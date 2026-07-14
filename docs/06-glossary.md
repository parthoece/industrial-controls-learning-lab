# Core Glossary

| Term | Working definition |
| --- | --- |
| Plant | The physical or simulated system being controlled |
| Setpoint | Desired value for a controlled variable |
| Measurement | Sensor or model value used as feedback |
| Error | Difference between setpoint and measurement |
| Controller | Algorithm that computes an actuator command |
| Sample time | Time between digital control updates |
| Saturation | Limit that prevents an actuator command exceeding available range |
| Anti-windup | Technique that prevents or unwinds integral accumulation during saturation |
| State machine | Explicit states and transitions representing equipment behavior |
| Operating mode | High-level selection such as manual, automatic, maintenance, or disabled |
| Interlock | Condition that blocks an operation until required conditions are satisfied |
| Functional safety | Risk-reduction functions implemented with appropriately designed and validated safety systems; not ordinary control logic |
| Axis | Logical motion object representing a motor/mechanism and its command/status interface |
| Homing | Procedure establishing a valid machine coordinate reference |
| Motion profile | Time-varying position, velocity, or acceleration reference |
| CiA 402 | Standardized drive profile defining states and control/status objects |
| EtherCAT working counter | Diagnostic value indicating expected datagram processing by slaves |
| Jitter | Variation in timing around the intended execution interval |
| Overrun | Failure to finish a cyclic task before its next deadline |
| Telemetry | Measurements and status transmitted for observation or storage |
| Traceability | Ability to reconstruct the history and context of a part, batch, or operation |
| OEE | Availability × performance × quality, calculated from explicit operational assumptions |
| Idempotency | Property that repeated processing of the same request does not duplicate its intended effect |
