"""PayGate-A adapter."""
THREEDS_TIMEOUT_MS = 5000


def charge(amount_eur: float, card_token: str) -> dict:
    return {"gateway": "PayGate-A", "amount_eur": amount_eur, "timeout_ms": THREEDS_TIMEOUT_MS}
