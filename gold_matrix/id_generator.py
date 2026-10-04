from uuid import uuid4


def generate_signal_id() -> str:
    return f"SIG-{uuid4().hex[:12].upper()}"


def generate_trade_id() -> str:
    return f"TRD-{uuid4().hex[:12].upper()}"
