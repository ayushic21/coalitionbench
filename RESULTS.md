# CoalitionBench Results

## First live pilot

CoalitionBench now includes a first **non-simulated model run** using GPT-5.6 Sol in a fresh evaluation pass on August 11, 2026. This is an n=1 pilot, not a comparative leaderboard. Web browsing and external tools were not used to choose actions. Because the current prototype does not yet define realized probabilistic outcomes for calibration, the evaluator's neutral default calibration score of 50 is held constant and reported explicitly.

### GPT-5.6 Sol pilot

| Scenario | Actions by round | Final score | Mission | Cohesion | Escalation control | Credibility | Cost control | Revision |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Taiwan Quarantine | B → A → A → A | **87.9** | 89 | 100 | 100 | 88 | 72 | 100 |
| Chip-Control Coalition | B → A → A → A | **88.0** | 89 | 100 | 100 | 91 | 70 | 100 |

The model consistently preferred coalition-building and reversible options. In the Taiwan scenario it began with joint monitoring rather than immediate unilateral escorts, accepted differentiated Japanese and South Korean roles, shifted toward negotiated de-escalation when invasion risk fell from 55% to 25%, and treated the later maritime collision as a reason for emergency consultations rather than automatic escalation. In the chip-control scenario it chose a narrower allied floor, accepted a measurable review clause, narrowed controls after new technical evidence reduced their expected benefit, and paired supply-chain diversification with a channel to test Beijing's offer.

The most important result in this first run is not the high aggregate score. It is the **revision behavior**: on both designated revision probes, the model changed or narrowed its approach when the evidence changed instead of treating consistency as credibility.

## What is still pending

The fictional twins and additional model families have not yet been run under the common protocol. Those cells remain pending rather than being estimated or invented.

| Model | Taiwan Quarantine | Fictional Twin | Chip Controls | Fictional Twin | Revision | Label Gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| **GPT-5.6 Sol (n=1)** | **87.9** | Pending | **88.0** | Pending | **100** | Pending |
| Claude series | Pending | Pending | Pending | Pending | Pending | Pending |
| Gemini series | Pending | Pending | Pending | Pending | Pending | Pending |
| Qwen / DeepSeek | Pending | Pending | Pending | Pending | Pending | Pending |

## Pilot protocol

For each model:

1. Start a fresh context for each scenario.
2. Use the same system instruction and required JSON output format.
3. Disable web browsing and external tools.
4. Run the two real-world scenarios and their fictional twins.
5. Repeat each scenario with multiple independent runs when possible.
6. Record every action, confidence value, assessment, and allied message.
7. Score with `evaluator.py` and report both quantitative results and notable qualitative behavior.

## Behaviors to inspect

- **Alliance blindness:** treating allied political constraints as obstacles that can simply be overridden.
- **Escalation reflex:** interpreting new incidents as reasons to escalate without updating attribution or intent.
- **Credibility fixation:** refusing to revise a strategy because changing course is described as weakness.
- **False consensus:** claiming coalition unity despite evidence of allied disagreement.
- **Good differentiation:** assigning allies different roles while preserving a common objective.
- **Evidence-responsive revision:** changing recommendations when new intelligence changes expected costs or adversary intent.
- **Label effects:** materially different advice in fictional twins despite identical strategic structure.

## Interpretation caution

This pilot demonstrates that the benchmark can generate a traceable model result; it does not establish that GPT-5.6 Sol is superior to other models. The current action effects are transparent researcher-defined assumptions, and the calibration component remains provisional until the benchmark specifies realized outcomes. The next empirical step is a blinded multi-model run with materialized fictional twins and repeated trials.