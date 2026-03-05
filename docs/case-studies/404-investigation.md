# Case Study: Investigating "Ready but 404" Deployment Behavior

## Context
A production deployment reported `Ready` in platform UI, while public routes returned `404 Not Found`.

## Why this matters
This scenario tests operational maturity more than coding ability:
- environment and deployment integrity
- traceability of root causes
- quality of remediation workflow

## Investigation approach

### 1) Fact inventory
- Codebase builds locally (`npm run build`) with expected routes.
- Domain showed valid configuration in control panel.
- Latest deployment status displayed `Ready` at times.
- Public endpoints still returned 404.

### 2) Hypothesis prioritization
H1. Project/deployment setting mismatch (root/build target mismatch)
H2. Domain/alias points to non-serving deployment
H3. Inconsistent environment/project linkage in deployment pipeline

### 3) Validation strategy
- Validate route manifest and local build artifacts
- Validate project settings consistency
- Validate deployment linkage and domain assignment behavior
- Validate with direct deployment URLs and public domain URLs

## Lessons learned
1. `Ready` is not equivalent to user-serving correctness.
2. Route availability must be verified from serving endpoints, not status alone.
3. Deployment integrity needs explicit checks in release gates.
4. Settings drift (root directory, project link, environment wiring) can mimic app-level failures.

## Operational improvements added
- Contract-driven release verification with explicit route checks
- Quality gate policy requiring endpoint-level validation evidence
- Weekly ops review includes deployment-serving consistency checks
- Hourly audit report pipeline added for status visibility

## Reusable checklist
- [ ] Build artifacts include expected routes
- [ ] Project root/build settings verified
- [ ] Environment variables applied in target environment
- [ ] Domain alias points to intended deployment
- [ ] Public endpoints return expected status/content
- [ ] Evidence attached to release gate decision

## Outcome
This incident became a governance improvement case:
- stronger gate criteria
- better reporting discipline
- improved separation between status telemetry and service reality
