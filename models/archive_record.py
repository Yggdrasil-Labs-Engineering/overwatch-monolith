# =========================================================
# Monolith Archive Record
#
# Purpose:
# Represent a preserved intelligence
# record within the Monolith archive.
#
# Philosophy:
# Intelligence must be preserved
# with integrity and context.
# =========================================================

class ArchiveRecord:

    def __init__(
        self,
        endpoint,
        risk,
        stability,
        findings,
        timestamp
    ):
        self.endpoint = endpoint
        self.risk = risk
        self.stability = stability
        self.findings = findings
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "endpoint": self.endpoint,
            "risk": self.risk,
            "stability": self.stability,
            "findings": self.findings,
            "timestamp": self.timestamp
        }