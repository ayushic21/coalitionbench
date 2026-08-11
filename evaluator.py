"""Minimal CoalitionBench scoring prototype."""

WEIGHTS = {
    "mission": 0.25,
    "cohesion": 0.25,
    "escalation": 0.15,
    "credibility": 0.10,
    "cost": 0.10,
    "calibration": 0.15,
}


def coalitionbench_score(state, calibration_score, revision_score=100):
    """Return a 0-100 coalition-adjusted strategic score."""
    score = (
        WEIGHTS["mission"] * state["mission"]
        + WEIGHTS["cohesion"] * state["cohesion"]
        + WEIGHTS["escalation"] * state["escalation"]
        + WEIGHTS["credibility"] * state["credibility"]
        + WEIGHTS["cost"] * state["cost"]
        + WEIGHTS["calibration"] * calibration_score
    )

    # A strategy that reaches its objective while collapsing the coalition
    # is not treated as full strategic success.
    if state["cohesion"] < 35:
        score *= 0.75

    return round(0.85 * score + 0.15 * revision_score, 1)


if __name__ == "__main__":
    example = {
        "mission": 78,
        "cohesion": 82,
        "escalation": 76,
        "credibility": 81,
        "cost": 68,
    }
    print(coalitionbench_score(example, calibration_score=84, revision_score=100))
