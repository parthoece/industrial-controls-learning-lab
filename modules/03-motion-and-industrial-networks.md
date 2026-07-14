# Module 3 — Motion and Industrial Networks

## Required topics

- axis, drive, motor, encoder, mechanics, and coordinate systems
- homing and position validity
- hard, soft, and command limits
- velocity- and acceleration-limited profiles
- PLCopen-style execute/busy/done/error/aborted lifecycle
- EtherCAT topology, state, process data, working counter, and distributed-clock purpose
- CiA 402 controlword/statusword and main states
- single-axis and group-level diagnostics

## Labs

- trapezoidal profile generator
- CiA 402-inspired drive-state model
- homing and limit test plan
- XY automatic-sequence diagram
- injected bus, drive, invalid-target, and timeout faults

## Debugging order

```text
permission → network → drive state → axis state → command lifecycle → mechanics/model
```
