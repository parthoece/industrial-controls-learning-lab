from __future__ import annotations

from dataclasses import dataclass


@dataclass
class FirstOrderPlant:
    """First-order plant: tau * dy/dt + y = gain * u + disturbance."""

    gain: float = 1.0
    time_constant: float = 1.0
    value: float = 0.0
    disturbance: float = 0.0

    def step(self, command: float, dt: float) -> float:
        if dt <= 0:
            raise ValueError("dt must be positive")
        if self.time_constant <= 0:
            raise ValueError("time_constant must be positive")
        derivative = (self.gain * command + self.disturbance - self.value) / self.time_constant
        self.value += derivative * dt
        return self.value
