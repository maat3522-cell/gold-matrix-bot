from config import MIN_CONFIDENCE
from strategy import DefaultStrategy


def create_strategy(name: str):
    if name == "default":
        return DefaultStrategy(
            min_confidence=MIN_CONFIDENCE
        )

    raise ValueError(
        f"Unknown strategy: {name}"
    )
