# Safety and Scope Boundary

This project teaches software architecture and simulated machine behavior. It does not implement functional safety.

## Included for learning

- simulated emergency-stop and guard inputs
- software motion permission
- limit and target validation
- fault latching and explicit reset
- stop/recovery state logic
- diagnostics and fault injection

## Not included

- machine risk assessment
- safety integrity or performance-level calculation
- safety-rated hardware, networks, drives, or PLC logic
- safe torque off validation
- guarding design
- electrical design review
- legal compliance, certification, or commissioning procedures

## Contribution rule

Any example that mentions safety must state whether it is simulated, standard control logic, or safety-rated logic. This repository accepts only the first two and must never imply certification.
