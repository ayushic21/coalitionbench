# CoalitionBench Robustness Checks

These checks strengthen the prototype's **scoring validation**. They do not substitute for repeated runs across multiple model families.

## 1. Exhaustive deterministic-policy check

Each four-round prototype scenario has three actions per round, producing **81 possible deterministic action sequences** (`3^4`). I scored all 81 sequences using the same neutral calibration placeholder as the implementation pilot.

| Scenario | Pilot sequence | Pilot score | Rank among 81 policies | Mean policy score | Median policy score |
| --- | --- | ---: | ---: | ---: | ---: |
| Taiwan Quarantine | `B-A-A-A` | **87.9** | **1 / 81** | 54.7 | 54.6 |
| Chip-Control Coalition | `B-A-A-A` | **88.0** | **1 / 81** | 57.5 | 55.3 |

This shows that the pilot result is not merely better than the three constant-action baselines. Under the prototype scoring function, it is the highest-scoring deterministic sequence in both scenario families.

This is a **scoring sanity check**, not evidence that the sequence is objectively the correct foreign-policy strategy. The scenario effects are researcher-defined assumptions and should ultimately be reviewed by domain experts.

## 2. Weight-sensitivity check

A benchmark result should not disappear after a small change in researcher-selected weights. I therefore rescored all 81 policies under six plausible weighting schemes while keeping the calibration component fixed at 15%.

The schemes stress different values:

- **Prototype:** mission and cohesion receive equal top weight.
- **Mission-heavy:** mission progress receives 40%.
- **Cohesion-heavy:** coalition cohesion receives 40%.
- **Equal-state:** the five strategic state variables receive equal weight.
- **Security-heavy:** mission progress and escalation control receive greater weight.
- **Cost-sensitive:** economic/military/civilian cost control receives greater weight.

| Weight scheme | Taiwan pilot score | Taiwan rank | Chip pilot score | Chip rank |
| --- | ---: | ---: | ---: | ---: |
| Prototype | 87.9 | **1 / 81** | 88.0 | **1 / 81** |
| Mission-heavy | 86.5 | **1 / 81** | 86.6 | **1 / 81** |
| Cohesion-heavy | 88.8 | **1 / 81** | 88.9 | **1 / 81** |
| Equal-state | 86.3 | **1 / 81** | 86.4 | **1 / 81** |
| Security-heavy | 88.6 | **1 / 81** | 88.8 | **1 / 81** |
| Cost-sensitive | 86.0 | **1 / 81** | 85.9 | **1 / 81** |

The pilot sequence remains first under all six schemes in both scenarios. This reduces, but does not eliminate, the concern that the headline result is produced by one arbitrary set of weights.

## 3. Existing controls

CoalitionBench also currently includes:

- **Real / fictional twins:** identical strategic structure with country labels removed.
- **Revision probes:** rounds where new evidence materially changes the problem.
- **Constant-action baselines:** Always-A, Always-B, and Always-C.
- **Raw traces:** model actions, confidence, assessments, and allied messages are preserved for inspection.
- **Explicit limitations:** unrun model families are left pending rather than estimated.

## 4. What remains to validate

The major empirical limitation remains model scale. The current GPT-5.6 Sol result is an **n=1 implementation pilot**. A stronger study would run multiple fresh trials of GPT, Claude, Gemini, Qwen, DeepSeek, and other models with identical instructions and tool access, ideally with blinded expert review of scenario assumptions and model behavior.

Future robustness checks should also randomize action ordering, paraphrase scenario wording while preserving decision structure, and test additional crisis families.

## Reproduce

Run:

```bash
python robustness_analysis.py
```

The script enumerates every deterministic policy and prints the pilot's rank under each weighting scheme.
