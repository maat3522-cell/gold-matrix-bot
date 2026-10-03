
from dataclasses import dataclass


@dataclass
class StrategyDecision:
    signal: str
    confidence: float
    reason: str


class DefaultStrategy:
    name = "default"

    def __init__(self, min_confidence: float):
        self.min_confidence = min_confidence

    def evaluate(self, score: float) -> StrategyDecision:

        if score >= self.min_confidence:
            return StrategyDecision(
                signal="BUY",
                confidence=score,
                reason="Bullish conditions detected",
            )

        if score <= -self.min_confidence:
            return StrategyDecision(
                signal="SELL",
                confidence=abs(score),
                reason="Bearish conditions detected",
            )

        return StrategyDecision(
            signal="WAIT",
            confidence=0,
            reason="No valid setup detected",
        )
