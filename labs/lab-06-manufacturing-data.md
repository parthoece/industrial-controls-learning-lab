# Lab 06 — OEE and Traceability

## Question

Which assumptions change OEE, and can a part history be reconstructed from events?

## Baseline

```bash
python -m industrial_controls_lab run manufacturing
```

## Experiments

- include or exclude planned downtime
- change ideal cycle time
- add rejected parts
- submit a duplicate event identifier
- query a single part's ordered event history

## Evidence

Show the formula inputs, result, event schema, duplicate policy, and one reconstructed part history.

## Prerequisites

- Weeks 16–17
- Read [Week 16 Sql Traceability](../learning/week-16-sql-traceability.md)
- Install the development environment

## Acceptance criteria

- OEE inputs are explicit; duplicate event ID is rejected; ordered part history is reconstructed.
- Evidence includes normal, boundary, and failure cases.
- Assumptions, units, sample time, and limitations are recorded.

## Report

Use [`templates/experiment-report.md`](../templates/experiment-report.md).
