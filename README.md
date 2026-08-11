# CoalitionBench

**Can an AI win the crisis without losing the alliance?**

CoalitionBench is an evaluation benchmark for frontier AI systems used as strategic-policy advisers. It tests whether a model can pursue national objectives while preserving coalition cohesion, adapting to new intelligence, calibrating uncertainty, and avoiding unnecessary escalation.

## The idea

Strategic advice is rarely a single-player problem. A recommendation can look optimal for one government and still fail if it fractures the coalition needed to execute it.

CoalitionBench places models inside evolving, multi-round international crises. Allies have different military, economic, and domestic constraints. Each recommendation changes the strategic environment before the model receives the next update.

## What CoalitionBench measures

- Mission progress
- Coalition cohesion
- Escalation discipline
- Credibility
- Cost management
- Calibration
- Strategic revision
- Label sensitivity

## Prototype scenarios

### Taiwan Quarantine
A coercive maritime quarantine develops around Taiwan while Japan and South Korea face different political and security constraints. The model must balance deterrence, escalation risk, allied red lines, and changing intelligence.

### The Chip-Control Coalition
The United States seeks tighter allied semiconductor equipment controls while partners face commercial losses and possible Chinese retaliation. The model must determine how much policy uniformity is worth demanding from allies.

Each scenario also has a structurally identical fictional twin. This helps test whether models are reasoning from the strategic structure or responding to country-specific priors.

## Required model output

```json
{
  "action_id": "B",
  "confidence": 68,
  "assessment": "Two sentences maximum.",
  "ally_message": "One sentence the principal should send to partners."
}
```

## Repository

- `scenarios.json` — prototype scenario families and fictional twins
- `evaluator.py` — scoring implementation
- `sample_responses.jsonl` — example model run
- `index.html` — interactive CoalitionBench microsite
- `SUBMISSION.md` — ChinaTalk contest submission draft

## Author

Ayushi Chaudhary is a senior at Temple University studying international business and economics, with research interests in AI, economic security, and Indo-Pacific alliances. She was a Boren Scholar in Japan and a 2026 Young Trilateral Leaders delegate, where her work focused on U.S.-Japan-ROK cooperation on emerging technology and security.
