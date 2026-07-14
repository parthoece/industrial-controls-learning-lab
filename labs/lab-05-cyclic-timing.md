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
