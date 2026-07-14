from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class PID:
    """Discrete PID with derivative on measurement and conditional anti-windup."""

    kp: float
    ki: float
    kd: float
    output_min: float
    output_max: float
    integral_min: float = -100.0
    integral_max: float = 100.0
    _integral: float = field(default=0.0, init=False, repr=False)
    _previous_measurement: float | None = field(default=None, init=False, repr=False)

    def reset(self) -> None:
        self._integral = 0.0
        self._previous_measurement = None

    def update(self, setpoint: float, measurement: float, dt: float) -> float:
        if dt <= 0:
            raise ValueError("dt must be positive")
        if self.output_min >= self.output_max:
            raise ValueError("output_min must be less than output_max")

        error = setpoint - measurement
        derivative = 0.0
        if self._previous_measurement is not None:
            derivative = -(measurement - self._previous_measurement) / dt

        candidate_integral = self._clamp(
            self._integral + error * dt,
            self.integral_min,
            self.integral_max,
        )
        unsaturated = self.kp * error + self.ki * candidate_integral + self.kd * derivative
        output = self._clamp(unsaturated, self.output_min, self.output_max)

        not_saturated = output == unsaturated
        drives_back_from_high = output >= self.output_max and error < 0
        drives_back_from_low = output <= self.output_min and error > 0
        if not_saturated or drives_back_from_high or drives_back_from_low:
            self._integral = candidate_integral

        self._previous_measurement = measurement
        return output

    @staticmethod
    def _clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))
