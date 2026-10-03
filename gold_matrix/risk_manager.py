from dataclasses import dataclass


@dataclass(frozen=True)
class RiskLimits:
    max_risk_percent: float
    max_daily_loss_percent: float
    max_open_positions: int


class RiskManager:

    def __init__(self, limits: RiskLimits):
        self.limits = limits

    def validate_risk(self, risk_percent: float) -> bool:
        return (
            risk_percent > 0
            and risk_percent <= self.limits.max_risk_percent
        )

    def validate_daily_loss(
        self,
        daily_loss_percent: float,
    ) -> bool:
        return (
            daily_loss_percent >= 0
            and daily_loss_percent <= self.limits.max_daily_loss_percent
        )

    def validate_open_positions(
        self,
        open_positions: int,
    ) -> bool:
        return (
            open_positions >= 0
            and open_positions <= self.limits.max_open_positions
        )
