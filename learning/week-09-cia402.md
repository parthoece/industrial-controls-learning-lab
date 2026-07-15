# Week 09 — CiA 402 Drive States

> **Guiding question:** Why must motion software understand the drive state before issuing a profile?

## Learning objectives

- Explain the purpose of a drive profile.
- Recognize the main state progression.
- Separate controlword, statusword, mode, and fault.
- Design a safe conceptual reset sequence.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Controlword** | Command bits that request drive-state transitions. |
| **Statusword** | Feedback bits describing drive state and conditions. |
| **Mode of operation** | Selected motion behavior. |
| **Fault reset** | Command requesting exit from fault after cause is clear. |
| **Operation enabled** | Drive state that permits torque-producing operation under the profile rules. |

## Mental model

Simplified learning path:

```text
Switch on disabled
  → Ready to switch on
  → Switched on
  → Operation enabled
  → Fault (from abnormal conditions)
  → Switch on disabled (after valid reset)
```

The real standard includes more states, masks, transitions, and mode behavior.

## Why a profile exists

A standard drive profile reduces device-specific interpretation of:

- state transitions
- command/status bits
- operating modes
- faults
- homing and motion objects

Implementation still depends on device and network mapping.

## Command and feedback

Never infer drive state from the last controlword.

Use:

- controlword sent
- statusword received
- decoded state
- mode command
- mode display
- fault code
- communication freshness

## Fault sequence

Conceptual recovery:

1. remove motion command
2. capture fault information
3. clear physical or configuration cause
4. request fault reset
5. verify state changed
6. re-enable through normal sequence
7. require a new motion command

## Layer boundary

Drive `Operation enabled` does not mean:

- axis is homed
- target is valid
- network is healthy forever
- machine permission is true
- mechanics are clear

## Worked example

Application sends target position while drive is `Switch on disabled`.

Correct result:

- motion command rejected or held
- reason identifies drive state
- enable sequence handled separately
- target is not assumed executed

## Common mistakes

- Writing controlword and assuming transition completed.
- Resetting fault without preserving diagnostic code.
- Combining drive state and machine state.
- Calling the simplified exercise a CiA 402 implementation.

## Practice

1. Create a statusword decoder table from vendor documentation.
2. List prerequisites above drive operation enabled.
3. Define a fault-injection test.

## Practical lab

[Lab 04 — Motion and drive state](../labs/lab-04-motion.md)

## Knowledge checks

1. **What confirms a drive transition?**

   <details><summary>Answer</summary>

   Decoded statusword feedback, not the command alone.

   </details>

2. **Why separate machine and drive states?**

   <details><summary>Answer</summary>

   They represent different layers and can be valid or faulty independently.

   </details>

3. **What should happen after fault reset?**

   <details><summary>Answer</summary>

   Return to a non-operational state and follow the normal enable sequence.

   </details>

4. **Is the repository model complete CiA 402?**

   <details><summary>Answer</summary>

   No. It is a small state exercise.

   </details>

## Deep study

- [CiA 402 overview](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control) — Primary profile overview.
- [EtherCAT CoE overview](https://www.ethercat.org/en/technology.html) — Read the CoE section to understand profile reuse over EtherCAT.
- [Repository drive model](../src/industrial_controls_lab/motion/drive.py) — Compare the simplified state exercise with the lesson boundary.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
