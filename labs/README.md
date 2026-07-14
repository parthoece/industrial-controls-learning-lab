# Learning Labs

Each lab has three layers:

1. **guided baseline** — run the included code
2. **controlled modification** — change one assumption or parameter
3. **evidence** — explain results with measurements and a failure case

| Lab | Guide | CLI name |
| --- | --- | --- |
| First-order plant | [Lab 01](lab-01-first-order-plant.md) | `plant` |
| PID and anti-windup | [Lab 02](lab-02-pid.md) | `pid` |
| Equipment state machine | [Lab 03](lab-03-machine-state.md) | `machine` |
| Drive state and profile | [Lab 04](lab-04-motion.md) | `motion` |
| Cyclic timing | [Lab 05](lab-05-cyclic-timing.md) | `timing` |
| OEE and traceability | [Lab 06](lab-06-manufacturing-data.md) | `manufacturing` |

Run all tests before and after changes:

```bash
pytest
```
