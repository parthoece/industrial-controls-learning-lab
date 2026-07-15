# Week 15 — OPC UA, MQTT, REST, and Event Integration

> **Guiding question:** Which communication pattern fits status, commands, telemetry, and events?

## Learning objectives

- Compare OPC UA, MQTT, and REST roles.
- Choose request/response versus publish/subscribe.
- Design idempotent command and event handling.
- Define retry and outage behavior.

## Key terms

| Term | Working meaning |
| --- | --- |
| **OPC UA** | Industrial interoperability architecture with services and information models. |
| **MQTT** | Lightweight publish/subscribe messaging protocol. |
| **REST** | Resource-oriented HTTP interaction style. |
| **Publish/subscribe** | Producers publish without direct knowledge of consumers. |
| **Idempotency** | Repeating a request does not duplicate its intended effect. |
| **Quality of Service** | Delivery behavior category; not complete business processing guarantee. |

## Mental model

| Need | Typical fit | Important caution |
| --- | --- | --- |
| Browse machine model | OPC UA | model and security configuration |
| Current values and alarms | OPC UA | subscriptions and data quality |
| Broadcast telemetry/events | MQTT | duplicates, retained messages, ordering |
| Query resources/report data | REST | latency, authentication, retries |
| Time-critical control | local controller | do not depend on enterprise network |

## OPC UA

Strengths:

- typed address space
- metadata and relationships
- client/server and PubSub options
- industrial security profiles
- companion specifications

Not automatically secure. Configuration matters.

## MQTT

Strengths:

- decoupled publishers and subscribers
- small protocol overhead
- retained message and session options
- delivery QoS levels

Application must still handle duplicates, ordering, schema, and authorization.

## REST

Useful for:

- configuration services
- reports
- work-order and recipe resources
- non-cyclic commands with clear acknowledgement

Avoid placing REST calls in the cyclic control calculation.

## Idempotent processing

Use:

- stable command/event ID
- deduplication store
- explicit result
- retry-safe operation
- audit timestamp

MQTT QoS 2 does not automatically make a manufacturing operation exactly once.

## Outage design

Define:

- buffer size
- retry schedule
- expiry
- reconnect behavior
- duplicate policy
- local autonomy
- data-loss alarm

## Worked example

Part-complete event has ID `evt-9001`.

Publisher retries after disconnect.

Consumer receives the same event twice.

Correct behavior: second insert is rejected by ID, but delivery attempt may still be acknowledged and audited.

## Common mistakes

- Choosing a protocol by popularity.
- Assuming transport QoS equals business exactly-once.
- Sending unversioned JSON.
- Using remote API availability as a machine run condition without explicit design.

## Practice

1. Choose protocols for recipe download, telemetry, and genealogy query.
2. Design an idempotency key.
3. Write outage behavior for a 30-minute broker loss.

## Practical lab

Use [Lab 06](../labs/lab-06-manufacturing-data.md) for duplicate-event behavior.

## Knowledge checks

1. **What is OPC UA strong at?**

   <details><summary>Answer</summary>

   Industrial information modeling, services, subscriptions, and interoperability.

   </details>

2. **What is MQTT strong at?**

   <details><summary>Answer</summary>

   Decoupled publish/subscribe messaging, especially telemetry and events.

   </details>

3. **Does MQTT QoS guarantee one database row?**

   <details><summary>Answer</summary>

   No. Application-level idempotency is still required.

   </details>

4. **Where should time-critical control remain?**

   <details><summary>Answer</summary>

   In the local control system.

   </details>

## Deep study

- [OPC UA overview](https://opcfoundation.org/about/opc-technologies/opc-ua/) — Primary architectural overview.
- [MQTT 5.0 specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html) — Primary standard. Read concepts, QoS, sessions, and retained messages.
- [MQTT.org](https://mqtt.org/) — Short protocol introduction and ecosystem links.
- [MDN REST glossary](https://developer.mozilla.org/en-US/docs/Glossary/REST) — Easy REST concept refresher.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
