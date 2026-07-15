# Lab 03 — Equipment State and Interlocks

## Question

How can a technician determine why a start request was rejected?

## Baseline

```bash
python -m industrial_controls_lab run machine
```

## Experiments

- open the simulated guard before start
- lose motion permission while running
- try resetting while the cause is still active
- verify clearing a fault does not automatically restart
- add a sequence timeout reason

## Evidence

Publish a state diagram, transition table, test cases, and observable block/fault reasons.

## Prerequisites

- Weeks 5–6
- Read [Week 06 Interlocks Alarms Recovery](../learning/week-06-interlocks-alarms-recovery.md)
- Install the development environment

## Acceptance criteria

- Blocked start has a reason; reset fails while cause is active; reset does not restart.
- Evidence includes normal, boundary, and failure cases.
- Assumptions, units, sample time, and limitations are recorded.

## Report

Use [`templates/experiment-report.md`](../templates/experiment-report.md).
