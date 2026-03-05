# Phase 2 — SubAgent Structure

## Objective
Operationalize manager layer by assigning focused SubAgents per department with contract-driven execution.

## Department SubAgent Assignment

### Planning Manager
- `Requirements Analyst`
- `Stakeholder Coordinator`
- `Roadmap Planner`

### Development Manager
- `Domain Architect`
- `Application Engineer`
- `Integration Engineer`

### Design Manager
- `UX Strategist`
- `UI System Designer`
- `Interaction Designer`

### QA-QC Manager
- `Test Strategist`
- `Automation QA Engineer`
- `Quality Auditor`

### DevSecOps Manager
- `CI-CD Engineer`
- `Security Engineer`
- `Reliability Engineer`

### Operations Manager
- `Service Operator`
- `Support Coordinator`
- `Knowledge Manager`

## SubAgent Contract Rule
Each SubAgent task must include:
1. Scope
2. Deliverables
3. Verification checks
4. Completion criteria
5. Report in `Done/Risks/Decisions/Next/ETA`

## Escalation
- SubAgent -> Manager when blocked > 1 cycle
- Manager -> Kuro for standards or release-impacting blockers
