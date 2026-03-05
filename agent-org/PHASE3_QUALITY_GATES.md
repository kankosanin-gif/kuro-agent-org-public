# Phase 3 — Quality Gate Operations

## Objective
Move from structure definition to enforced execution with measurable quality controls.

## Gate Definitions

### G1 — Requirement Gate
Owner: Planning Manager
Criteria:
- Requirements baseline approved
- Acceptance criteria defined
- Traceability IDs assigned
Fail conditions:
- Ambiguous/untestable requirements

### G2 — Architecture Gate
Owner: Development Manager
Criteria:
- Architecture description (42010) complete
- Bounded context map approved
- Critical decisions recorded
Fail conditions:
- Missing architecture rationale

### G3 — Quality Gate
Owner: QA-QC Manager
Criteria:
- Test strategy approved
- Requirement-test traceability coverage >= threshold
- Regression checks pass
Fail conditions:
- Critical test failures

### G4 — Security Gate
Owner: DevSecOps Manager
Criteria:
- Security checks completed
- No unresolved critical vulnerabilities
- Secrets/config compliance validated
Fail conditions:
- Critical security finding unresolved

### G5 — Release Gate
Owner: QA-QC Manager + Operations Manager
Criteria:
- All required gates passed
- Runbook updated
- Rollback plan verified
Fail conditions:
- Missing rollback or unresolved blocker

## Escalation Policy
- Any failed gate => immediate manager escalation
- Any repeated gate failure (>1 cycle) => Kuro decision required

## Evidence Policy
Every gate decision must include artifacts:
- reports
- logs
- test/security evidence
- decision notes
