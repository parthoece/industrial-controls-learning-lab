# Lab 05 — Cyclic Timing

## Question

How much does a general-purpose operating system vary around a requested loop period?

## Baseline

```bash
python -m industrial_controls_lab run timing
```

## Experiments

- compare 1 ms, 5 ms, and 20 ms requested periods
- add artificial CPU or I/O work
- compare sleep-based scheduling with a deadline-based loop
- count overruns

## Evidence

Report requested period, minimum/mean/maximum interval, standard deviation, overruns, platform, and why this is not proof of hard real-time performance.

## Prerequisites

- Week 11
- Read [Week 11 Cyclic Execution](../learning/week-11-cyclic-execution.md)
- Install the development environment

## Acceptance criteria

- Timing statistics and overruns are reported with platform details and no real-time claim.
- Evidence includes normal, boundary, and failure cases.
- Assumptions, units, sample time, and limitations are recorded.

## Report

Use [`templates/experiment-report.md`](../templates/experiment-report.md).
