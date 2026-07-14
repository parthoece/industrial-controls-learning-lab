# Equipment State Machine

```mermaid
stateDiagram-v2
    [*] --> IDLE
    IDLE --> READY: enable request and permission
    READY --> RUNNING: start edge
    RUNNING --> STOPPING: stop request
    STOPPING --> READY: controlled stop complete
    RUNNING --> FAULT: fault or permission lost
    READY --> FAULT: fault
    FAULT --> RESETTING: reset edge and cause cleared
    RESETTING --> IDLE: reset complete
    RESETTING --> FAULT: cause still active
```

Important properties:

- clearing a fault does not automatically restart motion
- commands are edges or explicitly acknowledged requests
- each blocked transition has an observable reason
- the state machine is separate from functional-safety logic
