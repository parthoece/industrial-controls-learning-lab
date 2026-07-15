import pytest

from industrial_controls_lab.realtime.cyclic import measure_cyclic_timing


def test_timing_stats_are_well_formed() -> None:
    stats = measure_cyclic_timing(period=0.001, cycles=3)
    assert stats.requested_period == 0.001
    assert stats.minimum_interval > 0
    assert stats.minimum_interval <= stats.mean_interval <= stats.maximum_interval
    assert stats.standard_deviation >= 0
    assert stats.overruns >= 0


def test_timing_validates_inputs() -> None:
    with pytest.raises(ValueError):
        measure_cyclic_timing(period=0, cycles=3)
    with pytest.raises(ValueError):
        measure_cyclic_timing(period=0.001, cycles=1)
