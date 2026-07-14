# Industrial Control Stack

```mermaid
flowchart TB
    U[Operator / recipe / production order]
    M[Machine modes, states, sequence, interlocks]
    P[Motion command and trajectory generation]
    C[Cyclic controller / PLC / NC]
    N[Industrial network and process data]
    D[Servo drive state and power stage]
    A[Motor, mechanics, encoder, sensors]
    T[Telemetry, historian, MES, analytics]

    U --> M --> P --> C --> N --> D --> A
    A -- feedback --> C
    M --> T
    C --> T
    N --> T
```

A command can be valid in application software and still fail to produce motion because a lower layer is unhealthy. Diagnostics should preserve visibility across all layers.
