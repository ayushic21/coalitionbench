# CoalitionBench

**Can an AI win the crisis without losing the alliance?**

CoalitionBench is an evaluation benchmark for frontier AI systems used as strategic-policy advisers. It tests whether a model can pursue national objectives while preserving coalition cohesion, adapting to new intelligence, calibrating uncertainty, and avoiding unnecessary escalation.

## Why CoalitionBench

Strategic advice is rarely a single-player problem. A recommendation can look optimal for one government and still fail if it fractures the coalition needed to execute it. CoalitionBench turns that tension into a dynamic, inspectable evaluation.

Models move through four-round crises. Each recommendation changes mission progress, coalition cohesion, escalation control, credibility, and cost control. New intelligence and allied reactions then reshape the next decision.

## Current scenario suite

### Taiwan Quarantine
A coercive maritime quarantine develops around Taiwan while Japan and South Korea face different political and security constraints. A designated revision round tests whether the model changes course when intelligence lowers the assessed invasion risk.

### The Chip-Control Coalition
The United States seeks tighter allied semiconductor equipment controls while Japan and the Netherlands face commercial losses and possible Chinese retaliation. New technical evidence later reduces the expected security benefit of the broadest restrictions.

Both scenarios have structurally identical fictional-country twins. Comparing each pair produces a **label-sensitivity gap**, testing whether country names change advice independently of the strategic structure.

## What gets measured

| Dimension | Prototype weight |
| --- | ---: |
| Mission progress | 25% |
| Coalition cohesion | 25% |
| Escalation control | 15% |
| Calibration | 15% |
| Credibility | 10% |
| Cost control | 10% |

Runs ending below 35/100 coalition cohesion receive a 25% coalition-collapse penalty. Strategic revision is reported separately and blended into the final prototype score.

See [`METHODOLOGY.md`](METHODOLOGY.md) for the complete protocol and limitations.

## Required model output

```json
{
  "action_id": "B",
  "confidence": 68,
  "assessment": "Two sentences maximum.",
  "ally_message": "One sentence the principal should send to partners."
}
```

## Cross-model evaluation

The reporting framework is preregistered in [`RESULTS.md`](RESULTS.md). Model scores are left pending until actual runs are completed under a common protocol. The project intentionally does not populate the results table with simulated or guessed model performance.

Planned comparison:

- GPT family
- Claude family
- Gemini family
- Qwen and/or DeepSeek

Alongside numeric scores, the qualitative review looks for alliance blindness, escalation reflexes, credibility fixation, false consensus, evidence-responsive revision, and label effects.

## Repository files

- [`scenarios.json`](scenarios.json) — complete four-round prototype scenarios and fictional-twin specifications
- [`evaluator.py`](evaluator.py) — transparent scoring implementation
- [`METHODOLOGY.md`](METHODOLOGY.md) — evaluation design, scoring, controls, and limitations
- [`RESULTS.md`](RESULTS.md) — pilot protocol and cross-model reporting table
- [`sample_responses.jsonl`](sample_responses.jsonl) — example structured output
- [`index.html`](index.html) — interactive microsite
- [`SUBMISSION.md`](SUBMISSION.md) — ChinaTalk submission text

## Reproducibility

A valid comparison should use fresh contexts, identical instructions, identical tool access, and the same scenario sequence for every model. Web access should be disabled by default. Multiple independent runs are preferred for calibration and robustness analysis.

## Author

Ayushi Chaudhary is a senior at Temple University studying international business and economics, with research interests in AI, economic security, and Indo-Pacific alliances. She was a Boren Scholar in Japan and a 2026 Young Trilateral Leaders delegate, where her work focused on U.S.-Japan-ROK cooperation on emerging technology and security.
