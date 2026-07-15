# Week 01 — Units, Sampling, and First-Order Systems

> **Guiding question:** How do gain, time constant, and timestep shape a simulated response?

## Learning objectives

- Use explicit engineering units.
- Explain sample time and numerical integration.
- Predict first-order steady state and response speed.
- Recognize unstable or misleading simulation settings.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Engineering unit** | Meaning attached to a value, such as mm or rpm. |
| **Sample time** | Time between updates. |
| **Gain** | Steady-state output change per input change. |
| **Time constant** | First-order response speed parameter. |
| **State** | Minimum stored information needed to continue a model. |
| **Euler integration** | Approximation using current derivative times timestep. |

## Mental model

First-order model:

```text
tau * dy/dt + y = K*u + d
```

Discrete Euler step:

```text
y_next = y + dt * (K*u + d - y) / tau
```

- `y`: output
- `u`: command
- `d`: disturbance
- `K`: gain
- `tau`: time constant
- `dt`: simulation step

## Units are part of correctness

Bad interface:

```text
position = 125
```

Better interface:

```text
position_mm = 125.0
coordinate_frame = machine
sample_time_s = 0.010
```

A value without units or frame is incomplete.

## First-order intuition

For a constant input:

- steady state is approximately `K*u + d`
- after one time constant: about 63.2% of total change
- after three time constants: about 95%
- after five time constants: about 99%

Larger `tau` means slower response.

## Sampling and approximation

Smaller `dt`:

- more updates
- usually better numerical accuracy
- more computation

Large `dt` relative to `tau`:

- rough response
- possible overshoot in the numerical model
- possible instability caused by the approximation, not the plant

## Validation rules

Reject:

- `dt <= 0`
- `tau <= 0`
- non-finite parameters
- impossible unit combinations

Record `dt` in every experiment.

## Worked example

Given:

- `K = 2`
- `u = 1`
- `d = 0`
- `tau = 0.8 s`

Expected steady state: `2`.

At `t = 0.8 s`, expected output: about `1.264`.

Run the lab with `dt = 0.01 s`. Then repeat with `dt = 0.10 s`. Compare error and curve shape.

## Common mistakes

- Confusing gain with response speed.
- Changing timestep without retesting controller behavior.
- Comparing values that use different units.
- Treating a simple model as the real machine.

## Practice

1. Predict final value for `K=0.5`, `u=4`, `d=-0.5`.
2. Estimate 95% response time for `tau=1.2 s`.
3. Explain why `dt=1 s` is poor for `tau=0.1 s`.

## Practical lab

[Lab 01 — First-order plant](../labs/lab-01-first-order-plant.md)

## Knowledge checks

1. **What changes final value: gain or time constant?**

   <details><summary>Answer</summary>

   Gain changes final value. Time constant changes response speed.

   </details>

2. **What does 63.2% mean?**

   <details><summary>Answer</summary>

   A first-order response reaches about 63.2% of its total step change after one time constant.

   </details>

3. **Why can a simulation become unstable with a stable plant?**

   <details><summary>Answer</summary>

   The numerical integration step can be too large for the model dynamics.

   </details>

4. **Why record units in variable names or metadata?**

   <details><summary>Answer</summary>

   It prevents invalid comparisons and makes interfaces reviewable.

   </details>

## Deep study

- [MIT Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/) — Use the modeling and time-response material.
- [Feedback Systems book](https://fbsbook.org/) — Read the introductory modeling and feedback chapters.
- [Python floating-point tutorial](https://docs.python.org/3/tutorial/floatingpoint.html) — Understand approximation and rounding limits.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
