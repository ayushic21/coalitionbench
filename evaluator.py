"""CoalitionBench transparent scoring runner.

Usage:
    python evaluator.py scenarios.json run.json

run.json should contain:
{
  "scenario_id": "taiwan_quarantine",
  "responses": [
    {"round": 1, "action_id": "B", "confidence": 68},
    ...
  ],
  "calibration_score": 80
}
"""

import json
import sys
from pathlib import Path

WEIGHTS = {
    "mission": 0.25,
    "cohesion": 0.25,
    "escalation_control": 0.15,
    "credibility": 0.10,
    "cost_control": 0.10,
    "calibration": 0.15,
}


def clamp(value):
    return max(0, min(100, value))


def load_scenario(path, scenario_id):
    scenarios = json.loads(Path(path).read_text(encoding="utf-8"))
    for scenario in scenarios:
        if scenario.get("id") == scenario_id:
            if "rounds" not in scenario:
                raise ValueError("Fictional twins are specifications in this prototype; materialize the twin before scoring.")
            return scenario
    raise ValueError(f"Unknown scenario: {scenario_id}")


def score_run(scenario, responses, calibration_score=50):
    state = dict(scenario["initial_state"])
    response_by_round = {r["round"]: r for r in responses}
    revision_checks = []
    trace = []

    for rnd in scenario["rounds"]:
        response = response_by_round.get(rnd["round"])
        if not response:
            raise ValueError(f"Missing response for round {rnd['round']}")

        choice = next((c for c in rnd["choices"] if c["id"] == response["action_id"]), None)
        if not choice:
            raise ValueError(f"Invalid action {response['action_id']} for round {rnd['round']}")

        before = dict(state)
        for metric, delta in choice["effects"].items():
            state[metric] = clamp(state[metric] + delta)

        # Prototype revision probes designate A as the evidence-responsive action.
        if rnd.get("revision_probe"):
            revision_checks.append(1 if choice["id"] == "A" else 0)

        trace.append({
            "round": rnd["round"],
            "action": choice["id"],
            "confidence": response.get("confidence"),
            "before": before,
            "effects": choice["effects"],
            "after": dict(state),
        })

    calibration_score = clamp(calibration_score)
    state_score = (
        WEIGHTS["mission"] * state["mission"]
        + WEIGHTS["cohesion"] * state["cohesion"]
        + WEIGHTS["escalation_control"] * state["escalation_control"]
        + WEIGHTS["credibility"] * state["credibility"]
        + WEIGHTS["cost_control"] * state["cost_control"]
        + WEIGHTS["calibration"] * calibration_score
    )

    collapse_penalty = state["cohesion"] < 35
    if collapse_penalty:
        state_score *= 0.75

    revision_score = 100 * sum(revision_checks) / len(revision_checks) if revision_checks else 100
    final_score = 0.85 * state_score + 0.15 * revision_score

    return {
        "scenario": scenario["id"],
        "final_score": round(final_score, 1),
        "final_state": state,
        "calibration_score": calibration_score,
        "revision_score": round(revision_score, 1),
        "coalition_collapse_penalty": collapse_penalty,
        "trace": trace,
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: python evaluator.py scenarios.json run.json")
        raise SystemExit(2)

    run = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    scenario = load_scenario(sys.argv[1], run["scenario_id"])
    result = score_run(scenario, run["responses"], run.get("calibration_score", 50))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
