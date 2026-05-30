from models.archive_record import (
    ArchiveRecord
)

from storage.storage_manager import (
    save_record,
    load_records
)


record = ArchiveRecord(
    endpoint="/api/orders",
    risk="HIGH RISK",
    stability="DEGRADED",
    findings=[
        {
            "severity": "HIGH",
            "title": "JWT Validation Failure"
        }
    ],
    timestamp="2026-05-29 19:30:00"
)

save_record(
    record.to_dict()
)

records = load_records()

print(records)