from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass
class TrapezoidalProfile:
    """Incremental velocity- and acceleration-limited position reference."""

    max_velocity: float
    max_acceleration: float
    position: float = 0.0
    velocity: float = 0.0

    def reset(self, position: float = 0.0) -> None:
        self.position = position
        self.velocity = 0.0

    def step(self, target: float, dt: float) -> float:
        if dt <= 0:
            raise ValueError("dt must be positive")
        if self.max_velocity <= 0 or self.max_acceleration <= 0:
            raise ValueError("profile limits must be positive")

        distance = target - self.position
        if abs(distance) < 1e-10 and abs(self.velocity) < 1e-10:
            self.position = target
            self.velocity = 0.0
            return target

        direction = 1.0 if distance >= 0 else -1.0
        stopping_distance = self.velocity * self.velocity / (2.0 * self.max_acceleration)
        same_direction = self.velocity == 0.0 or math.copysign(1.0, self.velocity) == direction

        if same_direction and abs(distance) <= stopping_distance:
            acceleration = -math.copysign(self.max_acceleration, self.velocity)
        else:
            acceleration = direction * self.max_acceleration

        next_velocity = self.velocity + acceleration * dt
        next_velocity = max(-self.max_velocity, min(self.max_velocity, next_velocity))
        if self.velocity != 0.0 and next_velocity != 0.0:
            if math.copysign(1.0, self.velocity) != math.copysign(1.0, next_velocity):
                next_velocity = 0.0

        next_position = self.position + next_velocity * dt
        crossed = (target - self.position) * (target - next_position) <= 0
        if crossed and abs(distance) <= max(abs(next_velocity * dt), 1e-9):
            self.position = target
            self.velocity = 0.0
        else:
            self.position = next_position
            self.velocity = next_velocity
        return self.position
