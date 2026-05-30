from security.integrity import generate_hash

# =========================================================
# Monolith Storage Manager
#
# Purpose:
# Persist archived intelligence records.
#
# Responsibilities:
# - Save records
# - Load records
# - Preserve archive history
# - Support integrity validation
#
# Philosophy:
# Intelligence must survive beyond
# the moment it was observed.
# =========================================================

import json
from pathlib import Path


ARCHIVE_FILE = (
    Path(__file__)
    .parent.parent
    / "archive"
    / "archive.json"
)


def save_record(record):
    """
    Save archive record.
    """

    records = load_records()

    hashed_record = {
        "record": record, 
        "hash": generate_hash(record)
    }

    records.append(hashed_record)

    with open(
        ARCHIVE_FILE,
        "w",
        encoding="utf-8"
    ) as archive:
        json.dump(
            records,
            archive,
            indent=4
        )


def load_records():
    """
    Load archived records.
    """

    if not ARCHIVE_FILE.exists():
        return []

    with open(
        ARCHIVE_FILE,
        "r",
        encoding="utf-8"
    ) as archive:
        return json.load(archive)