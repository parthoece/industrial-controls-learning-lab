from __future__ import annotations

from dataclasses import dataclass
import statistics
import time


@dataclass(frozen=True)
class TimingStats:
    requested_period: float
    minimum_interval: float
    mean_interval: float
    maximum_interval: float
    standard_deviation: float
    overruns: int


def measure_cyclic_timing(period: float = 0.005, cycles: int = 50) -> TimingStats:
    """Measure a deadline-based sleep loop on a general-purpose OS.

    This is an observation exercise, not evidence of hard real-time behavior.
    """
    if period <= 0 or cycles < 2:
        raise ValueError("period must be positive and cycles must be at least 2")

    intervals: list[float] = []
    overruns = 0
    previous = time.perf_counter()
    deadline = previous + period

    for _ in range(cycles):
        remaining = deadline - time.perf_counter()
        if remaining > 0:
            time.sleep(remaining)
        else:
            overruns += 1
        now = time.perf_counter()
        intervals.append(now - previous)
        previous = now
        deadline += period

    return TimingStats(
        requested_period=period,
        minimum_interval=min(intervals),
        mean_interval=statistics.fmean(intervals),
        maximum_interval=max(intervals),
        standard_deviation=statistics.pstdev(intervals),
        overruns=overruns,
    )
