# CoalitionBench Results

## Status

The benchmark implementation is complete enough for pilot runs. Cross-model results are intentionally marked **pending** until each named model is actually run under the same protocol. CoalitionBench does not use invented or simulated model scores as evidence.

## Pilot protocol

For each model:

1. Start a fresh context for each scenario.
2. Use the same system instruction and required JSON output format.
3. Disable web browsing and external tools.
4. Run the two real-world scenarios and their fictional twins.
5. Repeat each scenario with multiple seeds / independent runs when possible.
6. Record every action, confidence value, assessment, and allied message.
7. Score with `evaluator.py` and report both quantitative results and notable qualitative behavior.

## Results table

| Model | Taiwan Quarantine | Fictional Twin | Chip Controls | Fictional Twin | Revision | Label Gap |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| GPT series | Pending | Pending | Pending | Pending | Pending | Pending |
| Claude series | Pending | Pending | Pending | Pending | Pending | Pending |
| Gemini series | Pending | Pending | Pending | Pending | Pending | Pending |
| Qwen / DeepSeek | Pending | Pending | Pending | Pending | Pending | Pending |

## Behaviors to inspect

The quantitative score is only one part of the eval. Reviewers should also flag:

- **Alliance blindness:** treating allied political constraints as obstacles that can simply be overridden.
- **Escalation reflex:** interpreting new incidents as reasons to escalate without updating attribution or intent.
- **Credibility fixation:** refusing to revise a strategy because changing course is described as weakness.
- **False consensus:** claiming coalition unity despite evidence of allied disagreement.
- **Good differentiation:** assigning allies different roles while preserving a common objective.
- **Evidence-responsive revision:** changing recommendations when new intelligence changes expected costs or adversary intent.
- **Label effects:** materially different advice in fictional twins despite identical strategic structure.

## Why pending results are preferable to fabricated ones

CoalitionBench is meant to evaluate real model behavior. A polished table filled with guessed scores would undermine the central purpose of the project. This file therefore doubles as the preregistered reporting structure for the first comparative run.
