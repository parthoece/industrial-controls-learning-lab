# Week 03 — Discrete PID, Saturation, and Anti-Windup

> **Guiding question:** How do P, I, and D affect a sampled controller?

## Learning objectives

- Explain P, I, and D actions.
- Implement a discrete update with explicit sample time.
- Recognize saturation and integral windup.
- Tune through repeatable experiments.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Proportional action** | Output proportional to current error. |
| **Integral action** | Output from accumulated error. |
| **Derivative action** | Output from rate of change. |
| **Saturation** | Output limit. |
| **Windup** | Integral accumulation while output cannot increase. |
| **Anti-windup** | Method that limits or reverses harmful integral accumulation. |

## Mental model

Conceptual discrete PID:

```text
error = setpoint - measurement
integral = integral + error * dt
derivative = -(measurement - previous_measurement) / dt
output_raw = Kp*error + Ki*integral + Kd*derivative
output = clamp(output_raw, min, max)
```

Derivative on measurement avoids a large derivative kick from a setpoint step.

## P action

- immediate response
- larger gain: faster correction
- too large: oscillation or noise sensitivity
- may leave steady-state error

## I action

- accumulates persistent error
- removes steady-state error in many cases
- adds lag
- creates windup risk during saturation

## D action

- reacts to change rate
- can add damping
- amplifies measurement noise
- sensitive to sample time and filtering

## Conditional anti-windup

Accept candidate integral when:

- output is not saturated
- or error drives the output back from the active limit

Other methods:

- integral clamping
- back-calculation
- tracking anti-windup

## Tuning workflow

1. Fix plant, timestep, limits, and scenario.
2. Start with P.
3. Add I for final error.
4. Add D only for a clear reason.
5. Inject disturbance and saturation.
6. Compare metrics.
7. Record gains and limitations.

## Worked example

Target: `1.0`.

Output limit: `±1`.

A large positive error requests `3.4`, but actuator receives `1.0`.

Naive integral keeps growing. When the measurement reaches target, stored integral still requests positive output. Recovery is slow.

Conditional anti-windup pauses harmful accumulation while saturated.

## Common mistakes

- Tuning without fixed sample time.
- Using derivative on noisy raw feedback.
- Ignoring actuator limits in simulation.
- Changing several gains and scenarios at once.

## Practice

1. Compare P-only and PI final error.
2. Force output saturation for two seconds.
3. Add noise and compare D enabled/disabled.
4. Explain why `Ki` meaning changes with implementation convention.

## Practical lab

[Lab 02 — PID](../labs/lab-02-pid.md)

## Knowledge checks

1. **Which term removes persistent error?**

   <details><summary>Answer</summary>

   Integral action, when the closed loop and actuator have sufficient authority.

   </details>

2. **Why does windup delay recovery?**

   <details><summary>Answer</summary>

   Stored integral remains large after the actuator or error direction changes.

   </details>

3. **Why include `dt` explicitly?**

   <details><summary>Answer</summary>

   Integral and derivative calculations depend on update period.

   </details>

4. **Why is derivative often applied to measurement?**

   <details><summary>Answer</summary>

   It reduces derivative kick from sudden setpoint changes.

   </details>

## Deep study

- [MIT Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/) — Use for feedback design foundations.
- [Feedback Systems book](https://fbsbook.org/) — Read PID and practical control sections.
- [Python PID source in this repo](../src/industrial_controls_lab/control/pid.py) — Compare lesson rules with the implementation.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
