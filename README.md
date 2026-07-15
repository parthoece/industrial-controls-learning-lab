# Industrial Controls Learning Lab

[![CI](https://github.com/parthoece/industrial-controls-learning-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/parthoece/industrial-controls-learning-lab/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/Python-3.11%20%7C%203.12%20%7C%203.13-blue)](pyproject.toml)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](LICENSE)

Self-contained fundamentals lessons and simulation labs for software engineers entering industrial controls, motion-control software, and smart manufacturing.

The repository teaches the core concepts directly. Curated standards, official documentation, and university material support deeper study.

> [!IMPORTANT]
> Educational and simulation-first. Not production machine control. Not functional safety. Not a certified motion controller.
>
> Real machinery requires risk assessment, independent safety functions, qualified review, controlled commissioning, and current vendor documentation.

## Status

| Item | Current state |
| --- | --- |
| Maturity | Alpha |
| Version | `0.1.0` development snapshot |
| Lessons | 18 self-contained weekly lessons |
| Reviews | 6 module reviews with answer keys |
| Runnable labs | 6 Python labs |
| Structured Text | 4 vendor-neutral examples |
| CI | Ubuntu; Python 3.11, 3.12, 3.13 |
| Hardware required | No |
| Hardware validated | No |
| Public API | Unstable before 1.0 |

## What you will learn

- physical systems, units, sampling, and feedback
- first-order models and response measurements
- discrete PID, saturation, and anti-windup
- PLC scan behavior and Structured Text
- equipment states, modes, interlocks, alarms, and recovery
- motion profiles, homing, limits, EtherCAT, and CiA 402 concepts
- cyclic execution, deadlines, jitter, interfaces, and bounded queues
- OPC UA, MQTT, REST, SQL, traceability, OEE, and OT security

## Quick start

### Linux or macOS

```bash
git clone https://github.com/parthoece/industrial-controls-learning-lab.git
cd industrial-controls-learning-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Windows PowerShell

```powershell
git clone https://github.com/parthoece/industrial-controls-learning-lab.git
Set-Location industrial-controls-learning-lab
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### Verify

```bash
industrial-controls-lab list
pytest
```

Expected lab names:

```text
plant
pid
machine
motion
timing
manufacturing
```

Run one lab:

```bash
industrial-controls-lab run machine
```

## Learning path

| Week | Lesson | Evidence |
| ---: | --- | --- |
| 0 | [Industrial control stack](learning/week-00-industrial-control-stack.md) | Stack diagram and vocabulary |
| 1 | [Units, sampling, and first-order systems](learning/week-01-units-sampling-first-order.md) | Plant experiment |
| 2 | [Feedback and response metrics](learning/week-02-feedback-response-metrics.md) | Step-response report |
| 3 | [Discrete PID and anti-windup](learning/week-03-discrete-pid.md) | PID tuning report |
| 4 | [PLC scan and Structured Text](learning/week-04-plc-scan-structured-text.md) | ST program and scan trace |
| 5 | [Equipment states and modes](learning/week-05-equipment-states-modes.md) | State diagram and transition table |
| 6 | [Interlocks, alarms, and recovery](learning/week-06-interlocks-alarms-recovery.md) | Fault and recovery tests |
| 7 | [Industrial networks and process data](learning/week-07-industrial-networks.md) | Layer and topology diagram |
| 8 | [EtherCAT states and diagnostics](learning/week-08-ethercat.md) | Troubleshooting checklist |
| 9 | [CiA 402 drive states](learning/week-09-cia402.md) | State decoder and fault notes |
| 10 | [Profiles, homing, limits, and sequencing](learning/week-10-motion-profiles-homing.md) | Motion evidence package |
| 11 | [Cyclic execution and jitter](learning/week-11-cyclic-execution.md) | Timing report |
| 12 | [Controller interfaces and simulation](learning/week-12-controller-interfaces.md) | Hardware abstraction tests |
| 13 | [Concurrency, queues, configuration, and logging](learning/week-13-concurrency-configuration.md) | Architecture review |
| 14 | [Factory information layers](learning/week-14-factory-information-layers.md) | Information-flow diagram |
| 15 | [OPC UA, MQTT, REST, and events](learning/week-15-industrial-integration.md) | Protocol comparison |
| 16 | [SQL and production data models](learning/week-16-sql-traceability.md) | Schema and queries |
| 17 | [OEE, observability, OT security, and deployment](learning/week-17-oee-observability-security.md) | Metrics and capstone proposal |

Start with [Learning materials](learning/README.md). The [18-week roadmap](docs/00-learning-path.md) includes competency gates.

## Repository layout

```text
.
├── learning/                    # Complete weekly lessons, reviews, references
├── modules/                     # Module summaries and outcomes
├── labs/                        # Guided experiments and evidence requirements
├── src/industrial_controls_lab # Runnable Python examples
├── examples/structured-text/   # IEC 61131-3-style examples
├── examples/sql/               # Manufacturing schema example
├── tests/                       # Automated software and curriculum checks
├── docs/                        # Role map, safety, diagrams, policies
├── templates/                   # Experiment, ADR, reference, progress templates
├── progress/                    # Reusable learner tracker
└── .github/                    # CI and contribution workflows
```

## Implemented software

| Capability | Implementation | Automated check | Boundary |
| --- | --- | --- | --- |
| First-order plant | `control/plant.py` | convergence | simple Euler model |
| PID | `control/pid.py` | setpoint tracking | educational discrete PID |
| Error metrics | `control/metrics.py` | invalid input | RMS, max, final error |
| Motion permission | `machine/interlocks.py` | first block reason | standard logic only |
| Equipment state | `machine/state_machine.py` | controlled reset | small state model |
| Drive state | `motion/drive.py` | fault reset | CiA 402-inspired only |
| Position profile | `motion/profile.py` | target completion | incremental trapezoidal profile |
| Cyclic timing | `realtime/cyclic.py` | input validation | no real-time guarantee |
| OEE | `manufacturing/oee.py` | expected result | explicit assumptions |
| Traceability | `manufacturing/traceability.py` | duplicate rejection | in-memory event store |

## Quality checks

```bash
make check
```

Cross-platform equivalent:

```bash
python -m compileall -q src tests scripts
pytest
python scripts/check_repo.py
```

## Documentation

- [Learning materials](learning/README.md)
- [Deep-study references](learning/references/deep-study.md)
- [Role map](docs/01-role-map.md)
- [Portfolio evidence](docs/03-portfolio-evidence.md)
- [Safety boundary](docs/04-safety-boundary.md)
- [Glossary](docs/06-glossary.md)
- [Curriculum authoring guide](docs/09-curriculum-authoring-guide.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Governance](GOVERNANCE.md)

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). Significant curriculum, API, architecture, or policy changes begin with a proposal issue.

Contributions must:

- be original or properly cited
- state units, timing, and assumptions
- include normal and failure evidence when behavior changes
- label work as simulation, pseudocode, or hardware-tested
- avoid proprietary material and unsafe operational instructions

## Support and security

Use [SUPPORT.md](SUPPORT.md) for learning and setup questions.

Report vulnerabilities, exposed credentials, or hazardous operational behavior privately through [SECURITY.md](SECURITY.md).

## License

Apache License 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

## Disclaimer

Product and protocol names are used for education. Their marks belong to their owners. This project is independent and is not endorsed or certified by those organizations.
