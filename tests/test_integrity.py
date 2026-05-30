from security.integrity import (
    generate_hash,
    verify_hash
)

record = {
    "endpoint": "/api/orders",
    "risk": "HIGH RISK"
}

record_hash = generate_hash(
    record
)

print(
    f"Hash: {record_hash}"
)

print(
    verify_hash(
        record,
        record_hash
    )
)