from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto


class EquipmentState(Enum):
    IDLE = auto()
    READY = auto()
    RUNNING = auto()
    STOPPING = auto()
    FAULT = auto()
    RESETTING = auto()


@dataclass
class EquipmentStateMachine:
    state: EquipmentState = EquipmentState.IDLE
    fault_reason: str | None = None

    def enable(self, permission: bool) -> bool:
        if self.state is not EquipmentState.IDLE or not permission:
            return False
        self.state = EquipmentState.READY
        return True

    def start(self, permission: bool) -> bool:
        if self.state is not EquipmentState.READY or not permission:
            return False
        self.state = EquipmentState.RUNNING
        return True

    def request_stop(self) -> bool:
        if self.state is not EquipmentState.RUNNING:
            return False
        self.state = EquipmentState.STOPPING
        return True

    def stop_complete(self) -> bool:
        if self.state is not EquipmentState.STOPPING:
            return False
        self.state = EquipmentState.READY
        return True

    def trip(self, reason: str) -> None:
        self.fault_reason = reason
        self.state = EquipmentState.FAULT

    def reset(self, cause_cleared: bool) -> bool:
        if self.state is not EquipmentState.FAULT or not cause_cleared:
            return False
        self.state = EquipmentState.RESETTING
        self.fault_reason = None
        self.state = EquipmentState.IDLE
        return True
