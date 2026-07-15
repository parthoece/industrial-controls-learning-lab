# Week 07 — Industrial Networks and Process Data

> **Guiding question:** What makes an industrial control network different from a normal application network?

## Learning objectives

- Separate physical, data-link, application, and device-profile concerns.
- Explain cyclic process data and acyclic configuration.
- Identify freshness and quality requirements.
- Use a layered troubleshooting order.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Process data** | Cyclic command and status values. |
| **Mailbox or acyclic data** | Configuration and diagnostics outside the main process exchange. |
| **Topology** | Physical and logical device arrangement. |
| **Process image** | Mapped controller memory for I/O. |
| **Freshness** | Age of data relative to its intended use. |
| **Device profile** | Standard object and state behavior for a device class. |

## Mental model

```text
Application sequence
  ↓
Motion command lifecycle
  ↓
Axis abstraction
  ↓
Device profile / drive state
  ↓
Industrial Ethernet process data
  ↓
Cable, connectors, device electronics
  ↓
Motor, mechanics, feedback
```

## Cyclic versus acyclic

Cyclic:

- repeated on a schedule
- small, bounded data
- commands and feedback

Acyclic:

- parameter access
- identity
- detailed diagnostics
- firmware or files

Do not place slow configuration work in the critical control path.

## Process-data contract

Define for every signal:

- direction
- data type
- engineering unit
- scaling
- update period
- valid state
- freshness limit
- fail behavior

## Network health

Healthy communication is more than link-up.

Check:

- expected devices present
- correct state
- process exchange successful
- counters consistent
- data fresh
- device reports valid status

## Troubleshooting order

1. Power and physical link.
2. Topology and device identity.
3. Network state.
4. Process-data mapping.
5. Device profile state.
6. Application command.
7. Mechanics and feedback.

## Worked example

A drive Ethernet port has link, but motion is blocked.

Possible causes:

- device not in operational network state
- process-data mapping mismatch
- expected statusword not updating
- command uses stale feedback

“Cable connected” is only one layer.

## Common mistakes

- Equating Ethernet with TCP/IP.
- Treating link status as complete network health.
- Ignoring data age.
- Debugging application code before checking topology.

## Practice

1. Create a signal contract for target position.
2. List cyclic and acyclic data for a servo drive.
3. Build a layered checklist for a missing encoder value.

## Practical lab

Diagram exercise; prepare for [Lab 04](../labs/lab-04-motion.md).

## Knowledge checks

1. **Why separate cyclic and acyclic traffic?**

   <details><summary>Answer</summary>

   They have different timing, size, and predictability requirements.

   </details>

2. **What makes data stale?**

   <details><summary>Answer</summary>

   Its age exceeds the bound expected by the consumer.

   </details>

3. **Is link-up enough to permit motion?**

   <details><summary>Answer</summary>

   No. Device state, process exchange, freshness, drive state, and application conditions also matter.

   </details>

4. **What is a device profile?**

   <details><summary>Answer</summary>

   A standardized device object, state, and command/status behavior model.

   </details>

## Deep study

- [EtherCAT Technology Overview](https://www.ethercat.org/en/technology.html) — Read functional principle, process data, topology, and diagnosis.
- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — Review typical OT topologies and operational constraints.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
