# Week 10 — Motion Profiles, Homing, Limits, and Sequencing

> **Guiding question:** How can software generate a valid reference and know whether position is meaningful?

## Learning objectives

- Explain velocity and acceleration limits.
- Estimate stopping distance.
- Separate position value from coordinate validity.
- Design homing, soft-limit, and sequence checks.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Motion profile** | Time-varying reference for position, velocity, or acceleration. |
| **Homing** | Procedure that establishes coordinate reference. |
| **Position valid** | Coordinate can be trusted for the intended operation. |
| **Soft limit** | Software position boundary. |
| **Hard limit** | Physical or safety-related end constraint. |
| **Stopping distance** | Distance required to reduce velocity to zero under a deceleration limit. |

## Mental model

For constant deceleration magnitude:

```text
stopping_distance = velocity^2 / (2 * acceleration)
```

Trapezoidal profile phases:

```text
accelerate → constant velocity → decelerate
```

A short move may be triangular: no constant-velocity phase.

## Reference generation

A profile should respect:

- maximum velocity
- maximum acceleration
- target direction
- current velocity
- stopping distance
- timestep

Jerk limits are advanced follow-on work.

## Coordinate validity

Position number alone is not enough.

Track:

- homed / not homed
- coordinate frame
- encoder validity
- following error
- absolute-encoder state
- power-cycle behavior

## Limits

| Limit | Purpose |
| --- | --- |
| Command validation | reject impossible target before move |
| Soft limit | software boundary in valid coordinates |
| Physical limit switch | field input near travel end |
| Mechanical stop | last physical boundary; not a control strategy |

Safety-rated limits require appropriate safety engineering.

## Command lifecycle

Typical fields:

- execute
- busy
- done
- aborted
- error
- error code

A new command may abort, queue, or reject the current command. State the policy.

## XY sequence

Example sequence:

1. validate both axes
2. move X clear
3. move Y to station
4. verify both done
5. perform process
6. return

Each step needs timeout, abort, and recovery behavior.

## Worked example

Current velocity: `1.0 m/s`.

Maximum deceleration: `2.0 m/s²`.

Stopping distance: `0.25 m`.

If target is only `0.10 m` away, the controller must already decelerate. A profile that accelerates toward the target will overshoot.

## Common mistakes

- Using position before homing.
- Checking target only after motion starts.
- Ignoring current velocity during target reversal.
- Treating mechanical stop as normal positioning.

## Practice

1. Calculate stopping distance at 0.5, 1.0, and 2.0 m/s.
2. Define homing success and failure criteria.
3. Create an XY sequence with timeouts.

## Practical lab

[Lab 04 — Motion](../labs/lab-04-motion.md)

## Knowledge checks

1. **Why is position validity separate from position value?**

   <details><summary>Answer</summary>

   A numeric value can exist before the coordinate reference is established or after feedback becomes invalid.

   </details>

2. **What determines stopping distance?**

   <details><summary>Answer</summary>

   Velocity squared divided by twice the deceleration magnitude in the simple constant-deceleration model.

   </details>

3. **What is a triangular profile?**

   <details><summary>Answer</summary>

   A short move that begins deceleration before reaching maximum velocity.

   </details>

4. **What must a sequence step expose?**

   <details><summary>Answer</summary>

   Command status, completion condition, timeout, fault, abort, and recovery path.

   </details>

## Deep study

- [PLCopen Motion Control](https://www.plcopen.org/standards/motion-control/) — Read the function-block lifecycle and homing overview.
- [CiA 402 overview](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control) — Connect profile modes to drive state.
- [Repository profile](../src/industrial_controls_lab/motion/profile.py) — Inspect the incremental stopping-distance logic.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
