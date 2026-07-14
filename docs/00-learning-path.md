# 18-Week Learning Path

Assumption: five focused sessions per week, usually 45–75 minutes each. Treat the dates as flexible; gate reviews matter more than calendar speed.

## Weekly rhythm

| Day | Activity | Evidence |
| --- | --- | --- |
| Monday | Learn the main concept | Short explanation in your own words |
| Tuesday | Read official sources | Reference note with uncertainties |
| Wednesday | Implement a small example | Code, Structured Text, or schema |
| Thursday | Test and diagnose | Normal, boundary, and failure case |
| Friday | Consolidate and publish | Weekly note plus one portfolio artifact |

## Roadmap

| Week | Topic | Friday evidence |
| ---: | --- | --- |
| 0 | Industrial-control stack and CS-to-controls vocabulary | Stack diagram and glossary |
| 1 | Units, sampling, differential-equation intuition, first-order systems | First-order plant simulation |
| 2 | Feedback, stability intuition, disturbances, and time-response metrics | Step-response experiment report |
| 3 | Discrete PID, saturation, windup, anti-windup, and tuning | Reproducible PID tuning report |
| 4 | IEC 61131-3 concepts and Structured Text | Small ST program with test table |
| 5 | Equipment states, operating modes, commands, and transitions | Explicit state-machine diagram and code |
| 6 | Interlocks, alarms, reset, recovery, timeouts, and diagnostics | Motion-permission and fault-recovery tests |
| 7 | Industrial-network and process-data fundamentals | Layer/topology diagram and vocabulary table |
| 8 | EtherCAT states, working counter, process data, and diagnostics | EtherCAT troubleshooting checklist |
| 9 | CiA 402 states, controlword/statusword, and drive faults | State decoder and injected-fault notes |
| 10 | Profiles, homing, limits, PLCopen lifecycle, and XY sequencing | Single-axis concept plus XY sequence diagram |
| 11 | Cyclic execution, deadlines, latency, jitter, and overruns | Timing measurement report |
| 12 | Controller interfaces, hardware abstraction, and deterministic updates | Simulated axis interface and tests |
| 13 | Concurrency, bounded queues, configuration, logging, and testability | Controller-service architecture review |
| 14 | Factory information layers and OT/IT boundaries | Manufacturing information-flow diagram |
| 15 | OPC UA, MQTT, REST, event-driven integration, and idempotency | Protocol comparison and adapter sketch |
| 16 | SQL, time-series data, alarms, recipes, parts, cycles, and genealogy | Schema and sample queries |
| 17 | OEE, observability, cybersecurity basics, deployment, and capstone proposal | Metrics mini-lab and capstone handoff |

## Gate A — control foundation

Proceed when you can explain and measure:

- setpoint, measurement, error, plant, controller, and disturbance
- sample time and why changing it changes a digital controller
- rise time, overshoot, settling time, steady-state error, and RMS error
- saturation, integral windup, and anti-windup
- the difference between a model and the physical system

## Gate B — machine control

Proceed when you can:

- separate modes, states, commands, status, and diagnostics
- explain why interlocks are evaluated before motion commands
- latch a fault and require an explicit reset
- prevent automatic restart after a fault is cleared
- answer “why is motion blocked?” from observable reason codes

## Gate C — motion stack

Proceed when you can trace and debug:

```text
application sequence
  → motion function block / command lifecycle
  → axis or NC layer
  → EtherCAT process data
  → CiA 402 drive state
  → motor, mechanics, and feedback
```

## Gate D — PC-based controller

Proceed when you can:

- explain deadline, latency, jitter, and overrun
- separate cyclic control work from logging, databases, and APIs
- use interfaces or test doubles instead of hard-coding hardware access
- explain why a Python timing experiment is not proof of hard real-time behavior
- test stale data, communication loss, invalid configuration, and queue overflow

## Gate E — manufacturing software

Proceed when you can:

- distinguish current state, events, commands, and measurements
- model parts, cycles, recipes, alarms, and equipment assets
- explain the intended roles of OPC UA, MQTT, and REST
- calculate OEE from stated assumptions
- design auditability, retries, idempotency, health checks, and least privilege

## Gate F — capstone readiness

Start the separate capstone repository when:

- all five earlier gates have evidence
- your project problem and non-goals are written
- the architecture can be explained without product-specific jargon
- normal behavior and at least three fault scenarios have acceptance criteria
- the project can begin as simulation and later accept real hardware adapters
