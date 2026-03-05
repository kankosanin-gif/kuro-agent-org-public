# Phase 1 — RACI Matrix (Manager Layer)

Legend: R=Responsible / A=Accountable / C=Consulted / I=Informed

| Workflow | Planning Mgr | Development Mgr | Design Mgr | QA-QC Mgr | DevSecOps Mgr | Operations Mgr | Kuro |
|---|---|---|---|---|---|---|---|
| Requirements Baseline (29148) | R | C | C | C | C | C | A |
| Architecture Description (42010) | C | R | C | C | C | I | A |
| Domain Boundary Definition (DDD) | C | R | C | C | I | I | A |
| UI/UX Spec Freeze | C | C | R | C | I | I | A |
| Test Strategy & Traceability | C | C | C | R | C | I | A |
| Security/Compliance Review | I | C | I | C | R | C | A |
| CI/CD Readiness | I | C | I | C | R | C | A |
| Release Go/No-Go | I | C | I | R | C | C | A |
| Incident Response | I | C | I | C | C | R | A |
| Post-release Review | C | C | C | R | C | R | A |

## Gate Ownership
1. Requirement Gate: Planning Mgr (R), Kuro (A)
2. Architecture Gate: Development Mgr (R), Kuro (A)
3. Quality Gate: QA-QC Mgr (R), Kuro (A)
4. Security Gate: DevSecOps Mgr (R), Kuro (A)
5. Release Gate: QA-QC + Ops (R), Kuro (A)
