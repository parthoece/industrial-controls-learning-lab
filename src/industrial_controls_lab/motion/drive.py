from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class DriveState(Enum):
    SWITCH_ON_DISABLED = auto()
    READY_TO_SWITCH_ON = auto()
    SWITCHED_ON = auto()
    OPERATION_ENABLED = auto()
    FAULT = auto()


@dataclass
class SimulatedDrive:
    """Small CiA 402-inspired state exercise, not a complete implementation."""

    state: DriveState = DriveState.SWITCH_ON_DISABLED
    fault_reason: str | None = None

    def enable_operation(self) -> bool:
        if self.state is DriveState.FAULT:
            return False
        self.state = DriveState.READY_TO_SWITCH_ON
        self.state = DriveState.SWITCHED_ON
        self.state = DriveState.OPERATION_ENABLED
        return True

    def disable(self) -> None:
        if self.state is not DriveState.FAULT:
            self.state = DriveState.SWITCH_ON_DISABLED

    def inject_fault(self, reason: str) -> None:
        self.fault_reason = reason
        self.state = DriveState.FAULT

    def reset_fault(self, cause_cleared: bool) -> bool:
        if self.state is not DriveState.FAULT:
            return True
        if not cause_cleared:
            return False
        self.fault_reason = None
        self.state = DriveState.SWITCH_ON_DISABLED
        return True

    @property
    def operation_enabled(self) -> bool:
        return self.state is DriveState.OPERATION_ENABLED
