# Week 17 — OEE, Observability, OT Security, and Deployment

> **Guiding question:** How can manufacturing software report performance without hiding assumptions or operational risk?

## Learning objectives

- Calculate OEE from explicit assumptions.
- Design logs, metrics, traces, and health checks.
- Apply basic OT security principles.
- Define a small deployable capstone milestone.

## Key terms

| Term | Working meaning |
| --- | --- |
| **Availability** | Run time divided by planned production time. |
| **Performance** | Ideal production time divided by run time. |
| **Quality** | Good count divided by total count. |
| **Observability** | Ability to understand internal behavior from outputs. |
| **Least privilege** | Only the access required for the task. |
| **Defense in depth** | Several independent protective layers. |

## Mental model

```text
OEE = Availability × Performance × Quality

Availability = Run time / Planned production time
Performance = Ideal cycle time × Total count / Run time
Quality = Good count / Total count
```

Clamp or validate impossible values. Document every time boundary.

## OEE assumptions

State:

- planned production window
- planned downtime treatment
- run-time source
- ideal cycle time source
- good/reject classification
- rework policy
- product mix behavior
- clock/timezone rules

## Observability signals

Logs:

- discrete diagnostic events

Metrics:

- counters, gauges, histograms

Traces/correlation:

- command → machine event → production record

Health:

- alive, ready, degraded, dependencies, data freshness

## OT security basics

- inventory assets and communication paths
- segment networks
- least privilege
- unique credentials
- protect secrets
- signed and controlled updates
- backups and restore tests
- audit administrative changes
- manage remote access
- preserve safe and reliable operation

## Deployment boundary

A deployable service needs:

- configuration validation
- startup and shutdown behavior
- health endpoint
- logs and metrics
- backup/restore plan
- version and migration policy
- rollback
- resource limits

## Capstone first milestone

Keep release 0.1 small:

- simulated two-axis cell
- explicit state and fault model
- one part route
- event history
- OEE report
- read-only API
- three injected faults
- acceptance tests

## Worked example

Planned production: `480 min`.

Run time: `420 min`.

Ideal cycle: `1 min/part`.

Total: `400`.

Good: `390`.

- Availability: `0.875`
- Performance: `0.9524`
- Quality: `0.975`
- OEE: about `0.8125`

Changing planned downtime policy changes the result. The formula alone is not the full definition.

## Common mistakes

- Publishing OEE without assumptions.
- Using one health Boolean for every dependency.
- Connecting OT assets directly to the internet.
- Treating backups as valid without restore testing.

## Practice

1. Calculate OEE for two downtime policies.
2. Define five service health metrics.
3. Draw network zones for a small cell.
4. Write three capstone acceptance faults.

## Practical lab

[Lab 06 — Manufacturing data](../labs/lab-06-manufacturing-data.md)

## Knowledge checks

1. **Why can two correct OEE calculations differ?**

   <details><summary>Answer</summary>

   They can use different planned-time, ideal-cycle, rework, or quality assumptions.

   </details>

2. **What is the difference between alive and ready?**

   <details><summary>Answer</summary>

   Alive means the process runs; ready means it can perform intended service.

   </details>

3. **What is least privilege?**

   <details><summary>Answer</summary>

   Grant only the access needed for a defined responsibility.

   </details>

4. **What should the first capstone release prove?**

   <details><summary>Answer</summary>

   A small integrated simulation with explicit requirements, faults, tests, and evidence.

   </details>

## Deep study

- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) — Primary OT security guide.
- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) — Learn logs, metrics, traces, and context.
- [Google SRE monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/) — Deep study for practical service monitoring.
- [Vorne OEE guide](https://www.oee.com/) — Accessible OEE explanations; compare terminology with your stated assumptions.

## Exit criteria

Move on when you can:

- explain the guiding question without notes
- reproduce the worked example
- pass the knowledge checks
- complete the linked evidence
- state one limitation of the model
