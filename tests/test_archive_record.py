from models.archive_record import (
    ArchiveRecord
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
    timestamp="2026-05-30 19:00:00"
)

print(
    record.to_dict()
)