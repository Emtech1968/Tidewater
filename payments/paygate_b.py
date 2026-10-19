"""PayGate-B adapter. Lower processing fees than PayGate-A."""
THREEDS_TIMEOUT_MS = 3000   # vendor default


def charge(amount_eur: float, card_token: str) -> dict:
    return {"gateway": "PayGate-B", "amount_eur": amount_eur, "timeout_ms": THREEDS_TIMEOUT_MS}
