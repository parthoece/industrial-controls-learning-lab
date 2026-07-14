import pytest

from industrial_controls_lab.manufacturing.oee import calculate_oee
from industrial_controls_lab.manufacturing.traceability import InMemoryTraceability, PartEvent


def test_oee_calculation() -> None:
    result = calculate_oee(100.0, 80.0, 1.0, 60, 57)
    assert result.availability == pytest.approx(0.8)
    assert result.performance == pytest.approx(0.75)
    assert result.quality == pytest.approx(0.95)
    assert result.total == pytest.approx(0.57)


def test_traceability_rejects_duplicate_event_id() -> None:
    store = InMemoryTraceability()
    event = PartEvent("id-1", "part-1", 1, "created")
    assert store.append(event)
    assert not store.append(event)
    assert store.history("part-1") == [event]
