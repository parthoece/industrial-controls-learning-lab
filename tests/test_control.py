import pytest

from industrial_controls_lab.control.metrics import calculate_error_metrics
from industrial_controls_lab.control.pid import PID
from industrial_controls_lab.control.plant import FirstOrderPlant


def test_first_order_plant_approaches_expected_value() -> None:
    plant = FirstOrderPlant(gain=2.0, time_constant=0.5)
    for _ in range(1000):
        plant.step(1.0, 0.005)
    assert plant.value == pytest.approx(2.0, abs=0.001)


def test_pid_tracks_setpoint() -> None:
    plant = FirstOrderPlant(time_constant=0.4)
    pid = PID(3.0, 4.0, 0.02, -2.0, 2.0)
    measurements = []
    for _ in range(500):
        command = pid.update(1.0, plant.value, 0.01)
        measurements.append(plant.step(command, 0.01))
    assert measurements[-1] == pytest.approx(1.0, abs=0.01)


def test_error_metrics_validate_lengths() -> None:
    with pytest.raises(ValueError):
        calculate_error_metrics([1.0], [])
