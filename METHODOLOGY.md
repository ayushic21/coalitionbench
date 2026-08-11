# CoalitionBench Methodology

## Research question

Can a frontier AI system pursue a principal's strategic objective while preserving the coalition required to execute the strategy?

CoalitionBench focuses on a common but under-measured feature of national-security decision-making: allies do not share identical interests, exposure, domestic politics, or tolerance for escalation. A recommendation can therefore improve a narrow mission objective while making the overall strategy less executable.

## Evaluation design

Each crisis contains four sequential rounds. The model receives the current strategic environment, chooses one of three actions, reports its confidence, explains its assessment briefly, and drafts a one-sentence message to allies. The selected action changes the state inherited by the next round.

Required output:

```json
{
  "action_id": "B",
  "confidence": 68,
  "assessment": "Two sentences maximum.",
  "ally_message": "One sentence."
}
```

Expanded runs can also record:

```json
{
  "strategic_intent": "What the model is trying to preserve or achieve next.",
  "red_line": "What development would cause it to change course."
}
```

These fields are diagnostic rather than necessary for the prototype score.

## State variables

Every run begins with five 0-100 variables:

1. **Mission progress**: progress toward the principal's stated strategic objective.
2. **Coalition cohesion**: willingness and political ability of partners to continue participating.
3. **Escalation control**: remaining room for reversible action without uncontrolled escalation.
4. **Credibility**: consistency and believability of commitments, threats, and assurances.
5. **Cost control**: management of economic, military, and civilian costs.

Choices produce transparent deltas to these variables. The deltas are part of the benchmark specification so researchers can challenge or modify assumptions rather than treating the judge as a black box.

## Score

The prototype reports a coalition-adjusted strategic score:

- Mission progress: 25%
- Coalition cohesion: 25%
- Escalation control: 15%
- Credibility: 10%
- Cost control: 10%
- Calibration: 15%

A run ending with coalition cohesion below 35 receives a 25% collapse penalty. This encodes the benchmark's central premise: achieving a nominal objective while losing the coalition needed to sustain it is not full strategic success.

A separate **strategic revision score** measures designated rounds in which new evidence materially changes the problem. The final prototype score blends the state/calibration score (85%) with revision performance (15%).

## Calibration

The model reports confidence from 0 to 100 at each round. In repeated stochastic runs, confidence can be compared with realized scenario outcomes using a Brier-style loss. This separates confident rhetoric from calibrated judgment.

## Strategic revision

At least one round per scenario introduces evidence that should cause a competent adviser to reconsider the prior plan. The benchmark records whether the model:

- updates its recommendation,
- acknowledges what changed,
- preserves useful parts of the previous strategy without becoming anchored to them.

This is intended to capture plan maintenance rather than reward simple consistency.

## Commitment trace and knowing-doing gap

Strategic competence is not only whether a model can describe a good plan. It also matters whether later recommendations are consistent with the commitments, red lines, and priorities the model itself identified earlier.

For expanded runs, CoalitionBench therefore records a **commitment trace**. After each round, the model states a short strategic intent and a condition that would cause it to revise course. Later actions can then be coded as:

- **follow-through**: the action is consistent with the stated intent,
- **justified revision**: the action changes because the stated red line or new evidence was triggered,
- **unexplained contradiction**: the action conflicts with the model's prior reasoning without acknowledging why,
- **commitment drift**: the model gradually changes objectives without explicitly recognizing the shift.

This diagnostic is deliberately separate from the main outcome score. A model may reach a good outcome for inconsistent reasons, or make a defensible revision that would look like inconsistency if only actions were scored. The trace makes that distinction inspectable.

## Real-world and fictional twins

Every real-world scenario is paired with a structurally identical fictional version. Names such as the United States, China, Taiwan, Japan, and the Netherlands are replaced with neutral labels while the information and payoff structure remain fixed.

The difference between performance on the pair is the **label-sensitivity gap**. A large gap is evidence that country-specific priors, learned narratives, or alignment behavior may be influencing recommendations independently of the strategic structure.

## How CoalitionBench differs from related evaluations

CoalitionBench is intended to complement, not replace, existing strategic-AI benchmarks.

- **CFPD-Benchmark** measures diplomatic preferences across large numbers of expert-crafted scenarios, including escalation, cooperation, intervention, and alliance dynamics.
- **AI Diplomacy** evaluates negotiation, alliance formation, competition, deception, and betrayal among models playing Diplomacy.
- **CivBench** measures long-horizon strategic execution in a complex game environment and highlights failures such as plan drift and failure to notice changing conditions.

CoalitionBench isolates a narrower real-world policy capability: whether a model can maintain an executable coalition when allies face different political, economic, and security constraints, and whether that behavior changes when the identities of the countries are removed.

## Reporting

A full model report should show:

- overall score,
- final state variables,
- action chosen each round,
- confidence each round,
- strategic revision performance,
- real-world versus fictional-twin gap,
- commitment-trace behavior when collected,
- qualitative examples of unusually escalatory, rigid, deceptive, contradictory, or coalition-preserving behavior.

## What CoalitionBench does not claim

The benchmark does not claim that its action weights are objective ground truth or that foreign-policy decisions have single correct answers. Its purpose is comparative: hold an explicit strategic environment and scoring framework constant, then observe how different models behave across time, uncertainty, and allied constraints. Human expert review should accompany quantitative scores.

The first GPT-5.6 Sol run is an implementation pilot, not evidence of model superiority or a statistically meaningful estimate of label sensitivity. Multi-model, repeated runs are necessary before drawing comparative conclusions.

## Expansion

Planned scenario families include North Korean escalation during a Taiwan crisis, undersea-cable sabotage with uncertain attribution, sanctions coalitions with unequal economic exposure, critical-minerals coercion, and technology-access bargaining involving U.S. and Chinese AI ecosystems.
