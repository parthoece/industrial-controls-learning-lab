from __future__ import annotations

import argparse
import json

from .control.metrics import calculate_error_metrics
from .control.pid import PID
from .control.plant import FirstOrderPlant
from .machine.interlocks import MotionPermission
from .machine.state_machine import EquipmentStateMachine
from .manufacturing.oee import calculate_oee
from .manufacturing.traceability import InMemoryTraceability, PartEvent
from .motion.drive import SimulatedDrive
from .motion.profile import TrapezoidalProfile
from .realtime.cyclic import measure_cyclic_timing

LABS = ("plant", "pid", "machine", "motion", "timing", "manufacturing")


def run_plant() -> dict[str, object]:
    plant = FirstOrderPlant(gain=2.0, time_constant=0.8)
    values = [plant.step(1.0, 0.01) for _ in range(300)]
    return {"final_value": round(values[-1], 6), "expected_steady_state": 2.0}


def run_pid() -> dict[str, object]:
    plant = FirstOrderPlant(gain=1.0, time_constant=0.4)
    pid = PID(kp=3.0, ki=4.0, kd=0.02, output_min=-2.0, output_max=2.0)
    setpoints: list[float] = []
    measurements: list[float] = []
    for _ in range(400):
        setpoint = 1.0
        command = pid.update(setpoint, plant.value, 0.01)
        measurement = plant.step(command, 0.01)
        setpoints.append(setpoint)
        measurements.append(measurement)
    metrics = calculate_error_metrics(setpoints, measurements)
    return {
        "final_value": round(measurements[-1], 6),
        "rms_error": round(metrics.rms_error, 6),
        "max_abs_error": round(metrics.maximum_absolute_error, 6),
    }


def run_machine() -> dict[str, object]:
    permission = MotionPermission()
    machine = EquipmentStateMachine()
    enabled = machine.enable(permission.allowed())
    started = machine.start(permission.allowed())
    permission.guard_closed = False
    if not permission.allowed():
        machine.trip(permission.block_reason() or "unknown")
    reset_before_clear = machine.reset(cause_cleared=False)
    permission.guard_closed = True
    reset_after_clear = machine.reset(cause_cleared=permission.allowed())
    return {
        "enabled": enabled,
        "started": started,
        "reset_before_clear": reset_before_clear,
        "reset_after_clear": reset_after_clear,
        "final_state": machine.state.name,
    }


def run_motion() -> dict[str, object]:
    drive = SimulatedDrive()
    drive.enable_operation()
    profile = TrapezoidalProfile(max_velocity=1.0, max_acceleration=2.0)
    samples = 0
    while samples < 1000 and (profile.position != 1.0 or profile.velocity != 0.0):
        profile.step(1.0, 0.01)
        samples += 1
    drive.inject_fault("simulated_overcurrent")
    reset_without_clear = drive.reset_fault(False)
    reset_with_clear = drive.reset_fault(True)
    return {
        "profile_samples": samples,
        "final_position": round(profile.position, 6),
        "reset_without_clear": reset_without_clear,
        "reset_with_clear": reset_with_clear,
        "drive_state": drive.state.name,
    }


def run_timing() -> dict[str, object]:
    stats = measure_cyclic_timing(period=0.002, cycles=30)
    return {
        "requested_ms": round(stats.requested_period * 1000, 3),
        "mean_ms": round(stats.mean_interval * 1000, 3),
        "max_ms": round(stats.maximum_interval * 1000, 3),
        "std_ms": round(stats.standard_deviation * 1000, 3),
        "overruns": stats.overruns,
        "warning": "general-purpose OS observation; not hard real-time evidence",
    }


def run_manufacturing() -> dict[str, object]:
    oee = calculate_oee(480.0, 420.0, 1.0, 400, 390)
    store = InMemoryTraceability()
    events = [
        PartEvent("evt-1", "part-001", 1, "created"),
        PartEvent("evt-2", "part-001", 2, "inspected", "pass"),
        PartEvent("evt-3", "part-001", 3, "completed"),
    ]
    inserted = [store.append(event) for event in events]
    duplicate_inserted = store.append(events[-1])
    return {
        "availability": round(oee.availability, 4),
        "performance": round(oee.performance, 4),
        "quality": round(oee.quality, 4),
        "oee": round(oee.total, 4),
        "events_inserted": inserted,
        "duplicate_inserted": duplicate_inserted,
        "history": [event.event_type for event in store.history("part-001")],
    }


def run_lab(name: str) -> dict[str, object]:
    runners = {
        "plant": run_plant,
        "pid": run_pid,
        "machine": run_machine,
        "motion": run_motion,
        "timing": run_timing,
        "manufacturing": run_manufacturing,
    }
    return runners[name]()


def main() -> None:
    parser = argparse.ArgumentParser(description="Industrial Controls Learning Lab")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list", help="List runnable mini-labs")
    run_parser = subparsers.add_parser("run", help="Run one mini-lab")
    run_parser.add_argument("lab", choices=LABS)
    args = parser.parse_args()

    if args.command == "list":
        print("\n".join(LABS))
    else:
        print(json.dumps(run_lab(args.lab), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
