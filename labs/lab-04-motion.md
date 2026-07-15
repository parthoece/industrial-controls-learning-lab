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

## Prerequisites

- Weeks 9–10
- Read [Week 10 Motion Profiles Homing](../learning/week-10-motion-profiles-homing.md)
- Install the development environment

## Acceptance criteria

- Profile reaches target; velocity/acceleration limits are respected; fault reset requires cause clear.
- Evidence includes normal, boundary, and failure cases.
- Assumptions, units, sample time, and limitations are recorded.

## Report

Use [`templates/experiment-report.md`](../templates/experiment-report.md).
