# Module 4 — PC-Based Controller Software

## Required topics

- cyclic tasks and deadlines
- latency, jitter, overrun, and timing measurements
- real-time versus non-real-time responsibilities
- hardware abstraction and dependency injection
- bounded queues and stale-data handling
- configuration validation
- structured logging and diagnostics
- deterministic state updates
- tests using simulated hardware

## Labs

- measure loop jitter on a general-purpose OS
- isolate a controller interface from a plant implementation
- reject stale commands and invalid configuration
- test a bounded queue overflow policy
- show why database and API work should not execute inside the critical control calculation

## Scope boundary

The Python examples demonstrate architecture and measurement, not hard real-time guarantees.
