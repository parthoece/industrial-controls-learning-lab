from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class PartEvent:
    event_id: str
    part_id: str
    sequence: int
    event_type: str
    detail: str = ""


@dataclass
class InMemoryTraceability:
    """Tiny event store demonstrating idempotent event identifiers."""

    _events_by_id: dict[str, PartEvent] = field(default_factory=dict)

    def append(self, event: PartEvent) -> bool:
        if event.event_id in self._events_by_id:
            return False
        self._events_by_id[event.event_id] = event
        return True

    def history(self, part_id: str) -> list[PartEvent]:
        return sorted(
            (event for event in self._events_by_id.values() if event.part_id == part_id),
            key=lambda event: event.sequence,
        )
