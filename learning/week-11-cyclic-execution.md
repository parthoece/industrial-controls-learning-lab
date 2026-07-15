# Week 11 — Cyclic Execution, Deadlines, Jitter, and Overruns

> **Guiding question:** What does it mean for a controller update to be on time?

## Learning objectives

- Define period, deadline, latency, jitter, and overrun.
- Measure intervals without claiming real-time guarantees.
- Explain deadline-based scheduling versus repeated sleep.
- Separate average performance from worst case.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Period** | Desired time between task releases. |
| **Deadline** | Latest acceptable completion time. |
| **Latency** | Delay between expected and actual event. |
| **Jitter** | Variation around intended timing. |
| **Overrun** | Work does not finish before next required release. |
| **Determinism** | Known bounded behavior under defined conditions. |

## Mental model

```text
release n          deadline n
|----------------------|
     execution
     |--------|

release n+1
|----------------------|
```

Correct control requires correct result and acceptable time.

## Timing values

Record:

- requested period
- actual interval min/mean/max
- standard deviation
- deadline misses
- execution duration
- workload
- platform and power settings

## Average is insufficient

A mean of `1.00 ms` can hide:

- most intervals near `0.9 ms`
- rare intervals of `8 ms`

Control risk often depends on maximum and distribution tails.

## Drift

Repeated sleep:

```text
work → sleep(period) → work
```

Period becomes `work + sleep`.

Deadline-based loop:

```text
next_deadline += period
sleep until deadline
```

This reduces accumulated drift but does not create real-time guarantees.

## Critical-path split

Cyclic path:

- read validated inputs
- update state and control
- write bounded outputs

Non-critical path:

- database writes
- file logs
- API calls
- dashboards
- large serialization

## Worked example

Requested period: `2 ms`.

Measured:

- mean: `2.01 ms`
- max: `7.8 ms`
- overruns: `2`

Conclusion: useful host observation. Not evidence of a 2 ms hard deadline guarantee.

## Common mistakes

- Reporting only mean interval.
- Calling low latency real-time.
- Printing inside the timing loop.
- Using wall clock instead of a monotonic performance clock.

## Practice

1. Compare 1, 5, and 20 ms periods.
2. Add CPU work and count overruns.
3. Explain what a maximum interval means for control.

## Practical lab

[Lab 05 — Cyclic timing](../labs/lab-05-cyclic-timing.md)

## Knowledge checks

1. **What is an overrun?**

   <details><summary>Answer</summary>

   The task does not complete before the next required release or deadline.

   </details>

2. **Why use a monotonic clock?**

   <details><summary>Answer</summary>

   It is not adjusted by wall-clock corrections.

   </details>

3. **Does deadline scheduling guarantee real-time?**

   <details><summary>Answer</summary>

   No. It reduces drift but the OS and code still need bounded behavior.

   </details>

4. **Which statistic is most important?**

   <details><summary>Answer</summary>

   No single statistic. Use worst case, distribution, deadline misses, and conditions.

   </details>

## Deep study

- [ROS 2 Introduction to Real-time Systems](https://design.ros2.org/articles/realtime_background.html) — Clear explanation of deadlines, memory, I/O, and testing.
- [Python time module](https://docs.python.org/3/library/time.html) — Read `perf_counter` and monotonic clock details.
- [Linux kernel real-time documentation](https://docs.kernel.org/core-api/real-time/index.html) — Advanced OS-level follow-on.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
