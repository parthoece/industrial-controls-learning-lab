# Curated deep-study references

Access review: 2026-07-15.

The weekly lessons teach the fundamentals. These sources add standards detail, deeper mathematics, vendor behavior, and production context.

## How to use the list

- Read the linked weekly lesson first.
- Follow the suggested section, not the entire source.
- Write a [reference note](../../templates/reference-note.md).
- Mark general principles versus vendor-specific behavior.
- Check for newer revisions before production use.

## Control systems

### Start here

- [MIT OpenCourseWare — Feedback Systems](https://ocw.mit.edu/courses/6-302-feedback-systems-spring-2007/)
  - Use: feedback properties, time response, stability, design context.
  - Level: university / deep.

- [Feedback Systems: An Introduction for Scientists and Engineers](https://fbsbook.org/)
  - Use: modeling, feedback, PID, robustness.
  - Level: complete open textbook.

### Numerical and software detail

- [Python floating-point tutorial](https://docs.python.org/3/tutorial/floatingpoint.html)
  - Use: numerical approximation limits.

- [Python statistics module](https://docs.python.org/3/library/statistics.html)
  - Use: mean and standard deviation definitions used in timing experiments.

## PLC and machine control

- [PLCopen Logic](https://www.plcopen.org/standards/logic/)
  - Use: IEC 61131-3 standardization context.

- [Beckhoff TwinCAT 3 PLC manual](https://infosys.beckhoff.com/content/1033/tc3_plc_intro/index.html)
  - Use: task, program organization, Structured Text, data types.
  - Label: vendor-specific.

- [CODESYS programming language reference](https://content.helpme-codesys.com/en/CODESYS%20Development%20System/_cds_struct_reference_programming_languages.html)
  - Use: compare IEC language implementation details.
  - Label: vendor-specific.

## Motion and industrial networks

- [PLCopen Motion Control](https://www.plcopen.org/standards/motion-control/)
  - Use: command lifecycle, function blocks, homing, coordinated motion scope.

- [EtherCAT Technology Overview](https://www.ethercat.org/en/technology.html)
  - Use: on-the-fly processing, topology, distributed clocks, working counter, diagnostics.

- [CiA 402 drive profile overview](https://www.can-cia.org/can-knowledge/cia-402-series-canopen-device-profile-for-drives-and-motion-control)
  - Use: drive profile purpose, state and operating-mode concepts.

- [Beckhoff EtherCAT System Documentation](https://infosys.beckhoff.com/content/1033/ethercatsystem/index.html)
  - Use: concrete EtherCAT configuration and diagnostics.
  - Label: vendor-specific.

## PC-based controller software

- [ROS 2 — Introduction to Real-time Systems](https://design.ros2.org/articles/realtime_background.html)
  - Use: deadlines, memory, I/O, synchronization, and measurement.

- [Python `time` module](https://docs.python.org/3/library/time.html)
  - Use: monotonic clocks and `perf_counter`.

- [Linux kernel real-time documentation](https://docs.kernel.org/core-api/real-time/index.html)
  - Use: advanced OS mechanisms.

- [Python typing protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
  - Use: interface-driven design and test doubles.

- [Python logging cookbook](https://docs.python.org/3/howto/logging-cookbook.html)
  - Use: queue-based logging outside the critical path.

## Smart manufacturing and integration

- [OPC Foundation — OPC UA](https://opcfoundation.org/about/opc-technologies/opc-ua/)
  - Use: services, information models, security, client/server and PubSub.

- [OASIS MQTT 5.0 specification](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)
  - Use: sessions, QoS, retained messages, reason codes.

- [MQTT.org](https://mqtt.org/)
  - Use: short first introduction and ecosystem links.

- [MDN REST](https://developer.mozilla.org/en-US/docs/Glossary/REST)
  - Use: resource and request/response concepts.

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
  - Use: SQL, joins, aggregates, and transactions.

- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
  - Use: primary keys, unique IDs, checks, and foreign keys.

- [NIST SP 800-82 Rev. 3 — Guide to OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
  - Use: OT architecture, threats, segmentation, access control, and operational constraints.

- [ISA-95 Part 1 overview/product page](https://www.isa.org/products/ansi-isa-95-00-01-2010-iec-62264-1-mod-enterprise)
  - Use: enterprise-control integration models and terminology.
  - Note: full standard may require purchase.

- [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/)
  - Use: logs, metrics, traces, and context propagation.

- [Google SRE — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/)
  - Use: practical monitoring signals and alert design.

- [Vorne OEE](https://www.oee.com/)
  - Use: accessible OEE explanation and loss categories.
  - Check every formula against your documented assumptions.

## Safety and professional boundary

- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final)
  - Security guidance, not a functional-safety standard.

- Current machine, electrical, and functional-safety standards
  - Obtain through the applicable standards body, employer, integrator, or qualified safety engineer.
  - Do not use this repository as a substitute.
