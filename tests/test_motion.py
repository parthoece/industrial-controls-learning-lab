import pytest

from industrial_controls_lab.motion.drive import DriveState, SimulatedDrive
from industrial_controls_lab.motion.profile import TrapezoidalProfile


def test_profile_reaches_target() -> None:
    profile = TrapezoidalProfile(max_velocity=1.0, max_acceleration=2.0)
    for _ in range(1000):
        profile.step(1.0, 0.01)
        if profile.position == 1.0 and profile.velocity == 0.0:
            break
    assert profile.position == pytest.approx(1.0)
    assert profile.velocity == 0.0


def test_drive_fault_requires_cause_clear() -> None:
    drive = SimulatedDrive()
    assert drive.enable_operation()
    drive.inject_fault("test")
    assert not drive.reset_fault(False)
    assert drive.state is DriveState.FAULT
    assert drive.reset_fault(True)
    assert drive.state is DriveState.SWITCH_ON_DISABLED
