# Lab 04 — Motion Profile and Drive State

## Question

Why must a motion command consider both the generated reference and the drive state?

## Baseline

```bash
python -m industrial_controls_lab run motion
```

## Experiments

- change maximum velocity and acceleration
- reverse target direction before reaching the first target
- inject a drive fault during the profile
- attempt reset before clearing the fault cause
- add target-position validation and soft limits

## Evidence

Record profile duration, peak velocity, target error, drive transitions, and the first failed layer in each fault scenario.
