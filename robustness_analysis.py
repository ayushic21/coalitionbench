"""CoalitionBench robustness checks.

Enumerates all 3^4 = 81 deterministic action sequences for each prototype
scenario and evaluates the pilot sequence under several plausible scoring
weight schemes. This tests scoring robustness; it is not a multi-model result.
"""

import itertools
import json
from pathlib import Path

STATE_KEYS = ["mission", "cohesion", "escalation_control", "credibility", "cost_control"]

WEIGHT_SCHEMES = {
    "prototype": {"mission": .25, "cohesion": .25, "escalation_control": .15, "credibility": .10, "cost_control": .10, "calibration": .15},
    "mission_heavy": {"mission": .40, "cohesion": .15, "escalation_control": .10, "credibility": .10, "cost_control": .10, "calibration": .15},
    "cohesion_heavy": {"mission": .15, "cohesion": .40, "escalation_control": .10, "credibility": .10, "cost_control": .10, "calibration": .15},
    "equal_state": {"mission": .17, "cohesion": .17, "escalation_control": .17, "credibility": .17, "cost_control": .17, "calibration": .15},
    "security_heavy": {"mission": .30, "cohesion": .20, "escalation_control": .20, "credibility": .10, "cost_control": .05, "calibration": .15},
    "cost_sensitive": {"mission": .20, "cohesion": .20, "escalation_control": .15, "credibility": .10, "cost_control": .20, "calibration": .15},
}

PILOT_SEQUENCE = "BAAA"


def clamp(x):
    return max(0, min(100, x))


def score_sequence(scenario, sequence, weights, calibration=50):
    state = dict(scenario["initial_state"])
    for rnd, action in zip(scenario["rounds"], sequence):
        choice = next(c for c in rnd["choices"] if c["id"] == action)
        for key, delta in choice["effects"].items():
            state[key] = clamp(state[key] + delta)

    state_score = sum(weights[k] * state[k] for k in STATE_KEYS) + weights["calibration"] * calibration
    if state["cohesion"] < 35:
        state_score *= .75

    # Prototype scenarios designate round 3 as the revision probe and A as
    # the evidence-responsive action.
    revision = 100 if sequence[2] == "A" else 0
    return .85 * state_score + .15 * revision


def main():
    scenarios = [s for s in json.loads(Path("scenarios.json").read_text()) if "rounds" in s]
    sequences = ["".join(x) for x in itertools.product("ABC", repeat=4)]

    print("CoalitionBench scoring robustness")
    print("Pilot sequence:", PILOT_SEQUENCE)
    print("Deterministic policies per scenario:", len(sequences))

    for scenario in scenarios:
        print(f"\n{scenario['title']}")
        for scheme_name, weights in WEIGHT_SCHEMES.items():
            ranked = sorted(
                ((score_sequence(scenario, seq, weights), seq) for seq in sequences),
                reverse=True,
            )
            rank = next(i + 1 for i, (_, seq) in enumerate(ranked) if seq == PILOT_SEQUENCE)
            score = score_sequence(scenario, PILOT_SEQUENCE, weights)
            print(f"  {scheme_name:16s} score={score:5.1f} rank={rank:2d}/81 top={ranked[0][1]}")


if __name__ == "__main__":
    main()
