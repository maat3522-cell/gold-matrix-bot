from dataclasses import dataclass

from assets import AssetProfile


@dataclass(frozen=True)
class PositionSizeRequest:
    account_balance: float
    risk_percent: float
    stop_loss_points: float
    asset: AssetProfile


def calculate_position_size(
    request: PositionSizeRequest,
) -> float:

    if request.account_balance <= 0:
        raise ValueError(
            "Account balance must be greater than zero."
        )

    if request.risk_percent <= 0:
        raise ValueError(
            "Risk percent must be greater than zero."
        )

    if request.stop_loss_points <= 0:
        raise ValueError(
            "Stop loss points must be greater than zero."
        )

    if request.asset.tick_value <= 0:
        raise ValueError(
            "Asset tick value must be greater than zero."
        )

    risk_amount = (
        request.account_balance
        * request.risk_percent
        / 100
    )

    position_size = (
        risk_amount
        / (
            request.stop_loss_points
            * request.asset.tick_value
        )
    )

    return position_size
