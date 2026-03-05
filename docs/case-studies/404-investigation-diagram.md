# 404 Investigation Flow (Mermaid)

```mermaid
flowchart TD
    A[Symptom: Latest shows Ready] --> B[Public routes return 404]
    B --> C{Domain misconfig?}
    C -->|No| D[Domain shows valid production mapping]
    C -->|Yes| Z[Fix domain mapping]

    D --> E{App build broken?}
    E -->|No| F[Local build + route manifest OK]
    E -->|Yes| Y[Fix app build]

    F --> G{Deployment settings drift?}
    G -->|Likely| H[Check root/build/project linkage]
    H --> I[Re-deploy with normalized settings]
    I --> J[Re-verify public endpoints]
    J --> K{Routes return 200?}
    K -->|Yes| L[Close incident + capture lessons]
    K -->|No| M[Escalate to gate failure workflow]

    M --> N[Gate Failure Issue]
    N --> O[Root cause + mitigation + recovery ETA]
```

## Control insight
- A deployment status label is not sufficient evidence of serving correctness.
- Release gate must require endpoint-level verification artifacts.
