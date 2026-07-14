from industrial_controls_lab.machine.interlocks import MotionPermission
from industrial_controls_lab.machine.state_machine import EquipmentState, EquipmentStateMachine


def test_permission_reports_first_block_reason() -> None:
    permission = MotionPermission(guard_closed=False, network_healthy=False)
    assert permission.block_reason() == "guard_open"


def test_fault_reset_does_not_restart() -> None:
    machine = EquipmentStateMachine()
    assert machine.enable(True)
    assert machine.start(True)
    machine.trip("guard_open")
    assert not machine.reset(False)
    assert machine.reset(True)
    assert machine.state is EquipmentState.IDLE
