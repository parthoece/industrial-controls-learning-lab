# Lab 02 — Discrete PID and Anti-Windup

## Question

What happens to recovery when the actuator saturates and the integral term keeps accumulating?

## Baseline

```bash
python -m industrial_controls_lab run pid
```

## Experiments

- P-only, PI, and PID settings
- output limit at ±1 versus ±10
- anti-windup enabled versus an intentionally naive integral implementation
- measurement noise with derivative action
- 10 ms versus 50 ms sample time

## Evidence

Report rise time, overshoot, settling time, steady-state error, RMS error, saturation duration, and gain choices.
