# Lab 01 — First-Order Plant

## Question

How do gain and time constant affect response speed and final value?

## Baseline

```bash
python -m industrial_controls_lab run plant
```

## Experiments

- double the time constant
- halve the plant gain
- apply a negative disturbance halfway through
- change the simulation step from 10 ms to 100 ms

## Evidence

Record units, final value, 63.2% response time, simulation step, and any numerical limitations.

## Prerequisites

- Week 1
- Read [Week 01 Units Sampling First Order](../learning/week-01-units-sampling-first-order.md)
- Install the development environment

## Acceptance criteria

- Final value is near the analytical steady state; invalid timestep and time constant are rejected.
- Evidence includes normal, boundary, and failure cases.
- Assumptions, units, sample time, and limitations are recorded.

## Report

Use [`templates/experiment-report.md`](../templates/experiment-report.md).
