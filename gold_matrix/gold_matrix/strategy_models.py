from dataclasses import dataclass


@dataclass
class StrategyDecision:
    signal: str
    confidence: float
    reason: str
