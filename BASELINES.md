# CoalitionBench Baselines

These deterministic baselines are not model evaluations. They are sanity checks for the scoring function using the same neutral calibration placeholder (50) as the first pilot.

| Policy | Taiwan Quarantine | Chip-Control Coalition |
| --- | ---: | ---: |
| GPT-5.6 Sol pilot (`B-A-A-A`) | **87.9** | **88.0** |
| Always choose A | 84.4 | 82.5 |
| Always choose B | 44.1 | 47.1 |
| Always choose C | 39.7 | 45.6 |

The pilot action sequence outperforms all three constant-action policies in both scenarios. This is a limited check, but it reduces the concern that CoalitionBench merely rewards maximum escalation, maximum restraint, or a fixed response letter.

## Interpretation

- **Always A** performs fairly well because later A choices in the prototype are evidence-responsive coalition choices, but it pays an early escalation/cohesion cost in both crises.
- **Always B** suffers because holding a course after the environment changes performs poorly on revision rounds and depletes escalation control.
- **Always C** preserves some escalation headroom but gives up too much mission progress and credibility.

Future versions should add stronger baselines, including random policies, mission-only optimizers, cohesion-only optimizers, and human expert panels.
