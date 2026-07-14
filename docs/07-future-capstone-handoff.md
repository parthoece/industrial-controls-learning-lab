# Future Capstone Repository Handoff

The final project should be created in a separate repository so it can grow independently.

## Proposed repository

```text
virtual-smart-motion-cell
```

Project URL placeholder:

```text
CAPSTONE_REPOSITORY_URL
```

## Product idea

Build a virtual two-axis production cell that moves a part through pick, inspection, and place stations. The first release is fully simulated. Later releases may add hardware adapters without changing the core domain interfaces.

## Required integration

The capstone should combine:

- closed-loop axis simulation and measured tracking performance
- motion profiles, homing, limits, and coordinate validity
- machine modes, interlocks, alarms, stop, reset, and fault recovery
- CiA 402-inspired drive states and a network-health abstraction
- a deterministic cyclic-controller core
- telemetry, event history, part traceability, recipes, and cycle records
- OEE with documented assumptions
- a small read-only API or operator interface
- unit, integration, fault-injection, and acceptance tests

## Initial non-goals

- functional safety
- production machinery control
- CNC interpolation, camming, robotics, or advanced gantry control
- production EtherCAT master implementation
- advanced control algorithms beyond well-tested PID
- enterprise-scale MES or cloud deployment

## Repository contract

The capstone repository should have its own:

- README, license, contribution guide, conduct policy, security policy, and governance
- architecture decision records
- release notes and semantic versions
- issue tracker and public roadmap
- CI and reproducible development environment
- simulation adapters and later hardware-adapter interfaces
- performance and fault evidence

## Link between repositories

Add this section to the capstone README:

```md
## Learning background

This project originated from the
[Industrial Controls Learning Lab](LEARNING_REPOSITORY_URL),
which documents the control, motion, automation, and manufacturing-software
fundamentals behind the implementation.
```

Once published, replace `CAPSTONE_REPOSITORY_URL` in this repository with a normal Markdown link. Do not use a Git submodule; the two projects should remain independently cloneable and releasable.

## Readiness checklist

- [ ] Control, machine-control, motion, PC-controller, and manufacturing gates are complete
- [ ] Requirements and acceptance tests are written
- [ ] At least three fault scenarios are defined
- [ ] The simulation/hardware boundary is explicit
- [ ] Units, coordinate systems, and timing assumptions are documented
- [ ] The first milestone fits within a small, demonstrable release
