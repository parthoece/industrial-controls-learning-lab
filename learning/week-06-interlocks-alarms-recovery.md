# Week 06 — Interlocks, Alarms, Reset, and Recovery

> **Guiding question:** How can a technician answer “why is motion blocked?”

## Learning objectives

- Design ordered permission checks.
- Separate alarm, acknowledgement, reset, and cause clear.
- Latch faults correctly.
- Build a controlled recovery path.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Permission** | Computed authority for an action. |
| **Block reason** | Observable first or complete reason list. |
| **Alarm** | Reported abnormal condition. |
| **Acknowledgement** | Operator confirms alarm was seen. |
| **Reset** | Request to clear latched state after cause is gone. |
| **Timeout** | Failure when expected progress does not occur in time. |

## Mental model

Permission evaluation order:

```text
emergency-stop state
→ guard state
→ network health
→ drive health
→ axis validity
→ target validity
→ sequence conditions
```

The order is part of the diagnostic contract.

## Interlock design

A useful interlock result contains:

- `allowed`
- `primary_reason`
- optional `all_reasons`
- timestamp or scan
- relevant measured values

Keep reason codes stable for tests and HMI mapping.

## Alarm lifecycle

| Stage | Meaning |
| --- | --- |
| Active | abnormal cause exists |
| Latched | fault remains recorded |
| Acknowledged | operator saw it |
| Cause clear | input condition recovered |
| Reset | software accepts recovery request |
| Cleared | state returned to normal path |

## Reset rules

Reset should fail when:

- cause remains active
- required feedback is invalid
- reset is not allowed in current state
- recovery prerequisite is missing

Reset should not start motion.

## Timeout diagnostics

A timeout must state:

- expected progress
- start time
- limit
- last observed state
- likely layer

`timeout` alone is weak evidence.

## Worked example

Start is blocked because guard is open and network is unhealthy.

Primary reason may be `guard_open` because physical access protection is checked first.

The full diagnostic may include both reasons. The HMI should not require code inspection.

## Common mistakes

- Clearing a fault when the input cause remains active.
- Using acknowledgement as reset.
- Returning only `permission=false`.
- Using one timeout for an entire sequence.

## Practice

1. Define ordered reasons for a motion command.
2. Write a fault lifecycle table.
3. Add a timeout to a two-step sequence.

## Practical lab

[Lab 03 — Equipment state](../labs/lab-03-machine-state.md)

## Knowledge checks

1. **Why order interlocks?**

   <details><summary>Answer</summary>

   The order defines which reason is reported first and supports consistent troubleshooting.

   </details>

2. **Does acknowledgement clear a fault?**

   <details><summary>Answer</summary>

   No. It records that the alarm was seen.

   </details>

3. **What must be true before reset?**

   <details><summary>Answer</summary>

   The cause is cleared and recovery prerequisites are valid.

   </details>

4. **Why must reset not restart?**

   <details><summary>Answer</summary>

   Recovery and production start are separate operator intentions.

   </details>

## Deep study

- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — Use the safety, reliability, and OT-operational context.
- [Motion permission ST example](../examples/structured-text/FB_MotionPermission.st) — Review ordered reason evaluation.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
