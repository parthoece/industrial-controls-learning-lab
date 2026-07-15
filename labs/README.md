# Learning labs

Each lab has four outputs:

1. baseline run
2. controlled change
3. failure or diagnostic case
4. evidence report

| Lab | Guide | CLI | Source | Tests |
| --- | --- | --- | --- | --- |
| First-order plant | [Lab 01](lab-01-first-order-plant.md) | `plant` | [`plant.py`](../src/industrial_controls_lab/control/plant.py) | [`test_control.py`](../tests/test_control.py) |
| PID | [Lab 02](lab-02-pid.md) | `pid` | [`pid.py`](../src/industrial_controls_lab/control/pid.py) | [`test_control.py`](../tests/test_control.py) |
| Machine state | [Lab 03](lab-03-machine-state.md) | `machine` | [`state_machine.py`](../src/industrial_controls_lab/machine/state_machine.py) | [`test_machine.py`](../tests/test_machine.py) |
| Motion and drive | [Lab 04](lab-04-motion.md) | `motion` | [`profile.py`](../src/industrial_controls_lab/motion/profile.py) | [`test_motion.py`](../tests/test_motion.py) |
| Cyclic timing | [Lab 05](lab-05-cyclic-timing.md) | `timing` | [`cyclic.py`](../src/industrial_controls_lab/realtime/cyclic.py) | [`test_timing.py`](../tests/test_timing.py) |
| Manufacturing | [Lab 06](lab-06-manufacturing-data.md) | `manufacturing` | [`oee.py`](../src/industrial_controls_lab/manufacturing/oee.py) | [`test_manufacturing.py`](../tests/test_manufacturing.py) |

```bash
pytest
industrial-controls-lab list
```
