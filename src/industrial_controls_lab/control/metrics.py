from __future__ import annotations

from dataclasses import dataclass
import math
from collections.abc import Sequence


@dataclass(frozen=True)
class ResponseMetrics:
    rms_error: float
    maximum_absolute_error: float
    final_error: float


def calculate_error_metrics(setpoints: Sequence[float], measurements: Sequence[float]) -> ResponseMetrics:
    if len(setpoints) != len(measurements) or not setpoints:
        raise ValueError("setpoints and measurements must have the same non-zero length")
    errors = [sp - pv for sp, pv in zip(setpoints, measurements, strict=True)]
    return ResponseMetrics(
        rms_error=math.sqrt(sum(e * e for e in errors) / len(errors)),
        maximum_absolute_error=max(abs(e) for e in errors),
        final_error=errors[-1],
    )
