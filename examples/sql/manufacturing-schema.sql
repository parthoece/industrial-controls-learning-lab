-- Educational schema. Adapt types, retention, security, and migrations for production.

CREATE TABLE part (
    part_id TEXT PRIMARY KEY,
    serial_number TEXT NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL
);

CREATE TABLE production_cycle (
    cycle_id TEXT PRIMARY KEY,
    part_id TEXT NOT NULL REFERENCES part(part_id),
    equipment_id TEXT NOT NULL,
    recipe_id TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL,
    completed_at TIMESTAMPTZ,
    result TEXT CHECK (result IN ('pass', 'reject', 'aborted'))
);

CREATE TABLE part_event (
    event_id TEXT PRIMARY KEY,
    part_id TEXT NOT NULL REFERENCES part(part_id),
    sequence_number INTEGER NOT NULL,
    event_type TEXT NOT NULL,
    event_time TIMESTAMPTZ NOT NULL,
    detail JSONB NOT NULL DEFAULT '{}'::jsonb,
    UNIQUE (part_id, sequence_number)
);

CREATE INDEX part_event_history_idx
    ON part_event (part_id, sequence_number);

-- Reconstruct one part's ordered history.
SELECT sequence_number, event_type, event_time, detail
FROM part_event
WHERE part_id = 'part-001'
ORDER BY sequence_number;
