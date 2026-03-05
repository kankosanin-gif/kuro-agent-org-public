# Kuro Agent Organization — Portfolio Repository

This repository demonstrates a practical, standards-aligned agent operating model for software and product execution.

## What this repo showcases

- Agent organization design (Kuro + 6 manager departments + subagents)
- ISO-aligned governance artifacts:
  - ISO/IEC/IEEE 15288 (lifecycle process governance)
  - ISO/IEC/IEEE 29148 (requirements + traceability)
  - ISO/IEC/IEEE 42010 (architecture description)
  - ISO/IEC/IEEE 12207 (software implementation/testing/maintenance)
- Contract-driven execution model with explicit completion criteria
- Quality gates + KPI framework for operational control
- Security-aware operating principles (context discipline, minimal dependency model)

## Fast portfolio path

- [Portfolio Navigation (5 min route)](docs/PORTFOLIO_NAV.md)
- [Phase 1 Org Baseline](agent-org/PHASE1_ORG_CHART.md)
- [Phase 2 SubAgent Structure](agent-org/PHASE2_SUBAGENT_STRUCTURE.md)
- [Phase 3 Quality Gates](agent-org/PHASE3_QUALITY_GATES.md)
- [Case Study: Ready but 404](docs/case-studies/404-investigation.md)
- [Ops: Hourly Reporting](docs/ops/hourly-reporting.md)

## Repository map

- `agent-org/`
  - `PHASE1_*` — org baseline, manager charters, RACI
  - `PHASE2_*` — subagent structure, boot prompts, task contracts
  - `PHASE3_*` — quality gates, KPI framework, operating cadence
  - `AGENT_OPERATING_PRINCIPLES.md`
  - `KURO_ORG_PIXEL_ART.txt`
  - `OPENCLOW_FORK_RESEARCH.md`
  - `GITHUB_PORTFOLIO_POSITIONING.md`
  - `scripts/hourly_audit.py`
  - `hooks/run_hooks.py`
  - `reports/hourly-status.md`
- `docs/`
  - `PORTFOLIO_NAV.md`
  - `case-studies/404-investigation.md`
  - `case-studies/404-investigation-diagram.md`
  - `ops/hourly-reporting.md`
  - `ops/hooks.md`
- `.github/ISSUE_TEMPLATE/`
  - `task-contract.md`
  - `gate-failure.md`
  - `manager-weekly-review.md`

## Execution philosophy

1. Keep systems minimal and composable
2. Separate research from implementation
3. Use contract-based completion, not implicit done states
4. Prefer isolated short sessions over bloated long sessions
5. Escalate from SubAgent to Agent Team only when cross-functional ambiguity/risk is high

## Intended audience

- Engineering leaders implementing AI-agent workflows
- DevOps/Platform teams designing AI-assisted delivery operations
- Product organizations requiring traceability and controlled autonomy

## Status

Actively evolving as an operational portfolio.
