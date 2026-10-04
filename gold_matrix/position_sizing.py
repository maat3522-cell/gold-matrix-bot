from dataclasses import dataclass
import math

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

    if request.asset.point_size <= 0:
        raise ValueError(
            "Asset point size must be greater than zero."
        )

    if request.asset.tick_size <= 0:
        raise ValueError(
            "Asset tick size must be greater than zero."
        )

    if request.asset.tick_value <= 0:
        raise ValueError(
            "Asset tick value must be greater than zero."
        )

    if request.asset.volume_step <= 0:
        raise ValueError(
            "Asset volume step must be greater than zero."
        )

    if request.asset.min_volume <= 0:
        raise ValueError(
            "Asset minimum volume must be greater than zero."
        )

    if request.asset.max_volume < request.asset.min_volume:
        raise ValueError(
            "Asset maximum volume must be greater than or equal to minimum volume."
        )

    risk_amount = (
        request.account_balance
        * request.risk_percent
        / 100
    )

    stop_loss_price_distance = (
        request.stop_loss_points
        * request.asset.point_size
    )

    tick_count = (
        stop_loss_price_distance
        / request.asset.tick_size
    )

    loss_per_volume_unit = (
        tick_count
        * request.asset.tick_value
    )

    if loss_per_volume_unit <= 0:
        raise ValueError(
            "Calculated loss per volume unit must be greater than zero."
        )

    raw_position_size = (
        risk_amount
        / loss_per_volume_unit
    )

    stepped_position_size = (
        math.floor(
            raw_position_size
            / request.asset.volume_step
        )
        * request.asset.volume_step
    )

    position_size = round(
        stepped_position_size,
        8,
    )

    if position_size < request.asset.min_volume:
        position_size = request.asset.min_volume

    if position_size > request.asset.max_volume:
        position_size = request.asset.max_volume

    return position_size
