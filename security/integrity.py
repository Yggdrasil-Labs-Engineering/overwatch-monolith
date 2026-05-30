# =========================================================
# Monolith Integrity Engine
#
# Purpose:
# Generate and verify integrity hashes
# for archived intelligence records.
#
# Responsibilities:
# - Generate record hashes
# - Verify record integrity
# - Detect unauthorized modification
# - Support chain-of-custody validation
#
# Philosophy:
# Trust Nothing.
# Verify Everything.
# Preserve Truth.
# =========================================================

import hashlib
import json


def generate_hash(record):
    """
    Generate SHA256 integrity hash
    for an archived record.
    """

    serialized_record = json.dumps(
        record,
        sort_keys=True
    )

    return hashlib.sha256(
        serialized_record.encode()
    ).hexdigest()


def verify_hash(record, stored_hash):
    """
    Verify archived record integrity.
    """

    calculated_hash = generate_hash(
        record
    )

    return calculated_hash == stored_hash