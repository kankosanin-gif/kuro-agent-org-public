# OpenClaw Fork Research (Portfolio-Oriented)

## Context
Goal is not random forking; goal is to produce visible, high-signal improvements that demonstrate:
- systems thinking
- agent operations design
- secure automation practices
- practical developer UX impact

## Local doc areas reviewed
- `docs/tools/subagents.md`
- `docs/tools/skills.md`
- `docs/tools/acp-agents.md`
- `docs/tools/loop-detection.md`
- `docs/tools/reactions.md`
- `docs/tools/browser*.md`

## Candidate Fork Themes

### 1) Agent Org Governance Pack (high portfolio value)
Problem:
- Teams lack standard manager/subagent governance templates.
Proposal:
- Add an official "organization operating kit" with RACI, gates, and KPI templates.
Impact:
- Immediate adoption by teams scaling beyond solo-agent usage.

### 2) Contract-Driven Task Execution
Problem:
- Task completion criteria are often implicit.
Proposal:
- Add built-in task contract schema and validation checklist.
Impact:
- Better reliability, less drift, cleaner audit trails.

### 3) Context Budget Guardrails
Problem:
- Context bloat degrades output quality.
Proposal:
- Add optional context budget hints and route pruning for skills/rules.
Impact:
- More stable long-running workflows and lower token waste.

### 4) SubAgent vs Agent-Team Orchestration Mode
Problem:
- Users don’t know when to use a single delegate vs multi-agent collaboration.
Proposal:
- Introduce policy layer and docs with auto-escalation heuristics.
Impact:
- Better decomposition and execution efficiency.

### 5) Hourly Audit + Ops Reporting Mode
Problem:
- Operational visibility is inconsistent.
Proposal:
- Add lightweight scheduler-backed report generation templates.
Impact:
- Stronger ops trust and easier async management.

## Proposed Public Issue Backlog (for fork)
1. `feat(org-kit): add manager/subagent governance templates`
2. `feat(contract): add task contract schema and gate checks`
3. `feat(context): add context budget guardrails for skills routing`
4. `feat(orchestration): subagent/team selection policy and escalation`
5. `feat(ops): periodic audit report templates and scheduler hooks`

## Portfolio Positioning
This fork should be presented as:
"Agent Operations Layer on top of OpenClaw for standards-aligned engineering teams."
