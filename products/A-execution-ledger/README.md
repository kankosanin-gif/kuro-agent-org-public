# Product A — Agent Execution Ledger

A compact, evidence-first ledger model for tracking work-item progress across planning, execution, gate decisions, and release.

## Core Fields
- Work Item ID
- Contract ID
- Owner / Delegation
- Gate State (G1..G5)
- Evidence Links (Issue, PR, Logs, Report)
- Escalation Status (SLA breach / none)

## Why this exists
- Make delivery status auditable in one place
- Reduce ambiguity on "what is done"
- Speed up incident and review response

## Recommended Flow
1. Open work item + contract
2. Append proof-of-work per cycle
3. Record gate decision with rationale
4. Close only when evidence set is complete
