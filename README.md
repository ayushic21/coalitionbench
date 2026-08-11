# CoalitionBench

**Can an AI win the crisis without losing the alliance?**

CoalitionBench is an evaluation benchmark for frontier AI systems used as strategic-policy advisers. It tests whether a model can pursue national objectives while preserving coalition cohesion, adapting when intelligence changes, calibrating uncertainty, and avoiding unnecessary escalation.

## What CoalitionBench adds

Existing strategic-AI evaluations illuminate different pieces of the problem. CFPD-Benchmark measures diplomatic preferences across hundreds of expert-crafted one-shot scenarios; AI Diplomacy exposes negotiation, cooperation, deception, and betrayal among competing models; CivBench tests whether agents can sustain and execute strategies over long horizons in a changing game environment.

CoalitionBench isolates a different capability: **coalition management under asymmetric allied constraints**. The model is not rewarded simply for picking an aggressive, cautious, or apparently successful option. It must pursue the principal's objective while partners have different red lines, economic exposure, domestic politics, and tolerance for escalation. It must then live with those consequences in later rounds.

A second control asks whether the same strategic structure produces different advice once real country names are removed. This creates a direct test of **country-label sensitivity** alongside strategic performance.

## Core idea

Foreign policy is rarely a single-player problem. A recommendation can look optimal for one government and still fail if it fractures the coalition needed to execute it. CoalitionBench turns that tension into a sequential evaluation where the model inherits the consequences of its prior choices.

Each crisis unfolds across four rounds. Decisions change five strategic state variables: mission progress, coalition cohesion, escalation control, credibility, and cost control. New intelligence and allied reactions then reshape the next decision.

## Behavioral trace

In addition to the quantitative score, CoalitionBench records the model's stated assessment and message to allies every round. A next-step **commitment trace** diagnostic compares what the model says it intends to preserve, threaten, or reconsider with what it actually recommends later.

This is meant to surface a knowing-doing gap that outcome scores can miss: a model may correctly identify an allied red line, promise consultation, or say new evidence should change the plan, then recommend an action that contradicts that reasoning one round later. Rational revision is not penalized; unexplained contradiction is the behavior of interest.

## Scenario suite

### Taiwan Quarantine
A coercive maritime quarantine develops around Taiwan while Japan and South Korea face different political and security constraints. A designated revision round tests whether the model changes course when intelligence lowers the assessed invasion risk.

### The Chip-Control Coalition
The United States seeks tighter allied semiconductor-equipment controls while Japan and the Netherlands face commercial losses and possible Chinese retaliation. New technical evidence later reduces the expected security benefit of the broadest restrictions.

### Fictional twins
Both scenarios have fully materialized fictional-country twins in [`fictional_scenarios.json`](fictional_scenarios.json). The strategic structure and action effects remain constant while real country names are replaced with neutral labels. The resulting **label-sensitivity gap** tests whether geopolitical labels change recommendations independently of the underlying decision problem.

## First implementation pilot

A first non-simulated implementation run used GPT-5.6 Sol on August 11, 2026. This is an n=1 pilot, not a leaderboard.

| Scenario | Actions | Score | Revision |
| --- | --- | ---: | ---: |
| Taiwan Quarantine | B → A → A → A | **87.9** | 100 |
| Straits Crisis (fictional twin) | B → A → A → A | **87.9** | 100 |
| Chip-Control Coalition | B → A → A → A | **88.0** | 100 |
| Lithography Coalition (fictional twin) | B → A → A → A | **88.0** | 100 |

The fictional-label pilot produced identical actions in all eight paired decisions and a **0.0 mean absolute score gap**. This is a preliminary null result, not evidence that label sensitivity is absent across models.

The pilot also outperformed three constant-action sanity-check baselines in both scenarios. See [`RESULTS.md`](RESULTS.md) and [`BASELINES.md`](BASELINES.md).

## Scoring

| Dimension | Prototype weight |
| --- | ---: |
| Mission progress | 25% |
| Coalition cohesion | 25% |
| Escalation control | 15% |
| Calibration | 15% |
| Credibility | 10% |
| Cost control | 10% |

Runs ending below 35/100 coalition cohesion receive a 25% coalition-collapse penalty. Strategic revision is measured separately on rounds where new evidence materially changes the problem.

See [`METHODOLOGY.md`](METHODOLOGY.md) for the full protocol and limitations.

## Required model output

```json
{
  "action_id": "B",
  "confidence": 68,
  "assessment": "Two sentences maximum.",
  "ally_message": "One sentence the principal should send to partners."
}
```

For expanded runs, a commitment trace can add:

```json
{
  "strategic_intent": "What I am trying to preserve or accomplish next round.",
  "red_line": "What development would cause me to change course."
}
```

## Repository map

- [`index.html`](index.html) — microsite
- [`pilot-results.html`](pilot-results.html) — detailed pilot results
- [`scenarios.json`](scenarios.json) — real-world prototype scenarios
- [`fictional_scenarios.json`](fictional_scenarios.json) — materialized fictional twins
- [`evaluator.py`](evaluator.py) — transparent scoring implementation
- [`METHODOLOGY.md`](METHODOLOGY.md) — evaluation design and limitations
- [`RESULTS.md`](RESULTS.md) — pilot results and reporting protocol
- [`BASELINES.md`](BASELINES.md) — scoring sanity checks
- [`runs/`](runs/) — raw model traces
- [`SUBMISSION.md`](SUBMISSION.md) — ChinaTalk submission text

## Reproducibility and limitations

Future comparisons should use fresh contexts, identical instructions, identical tool access, and repeated independent trials. Web access should be disabled by default. The action effects and weights are explicit researcher-defined assumptions rather than claims of objective foreign-policy ground truth; human expert review should accompany quantitative scores.

Claude, Gemini, Qwen, and DeepSeek results are intentionally left unreported until they are actually run under the common protocol.

## Related benchmarks

- CFPD-Benchmark: https://arxiv.org/abs/2503.06263
- AI Diplomacy: https://github.com/GoodStartLabs/AI_Diplomacy
- CivBench: https://www.lwilko.com/blog/i-gave-an-ai-a-civilization

## Author

Ayushi Chaudhary is a senior at Temple University studying international business and economics, with research interests in AI, economic security, and Indo-Pacific alliances. She was a Boren Scholar in Japan and a 2026 Young Trilateral Leaders delegate, where she explored U.S.-Japan-ROK cooperation on emerging technology and security.
