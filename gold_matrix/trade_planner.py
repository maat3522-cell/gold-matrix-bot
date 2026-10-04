from market import MarketContext
from trade_plan import TradePlan
from risk_manager import RiskManager
from position_sizing import (
    PositionSizeRequest,
    calculate_position_size,
)


def build_trade_plan(
    context: MarketContext,
    direction: str,
    entry_price: float,
    stop_loss_points: float,
    take_profit_points: float,
    account_balance: float,
    risk_percent: float,
    risk_manager: RiskManager,
) -> TradePlan:

    if not risk_manager.validate_risk(risk_percent):
        raise ValueError(
            "Risk percent exceeds allowed risk limits."
        )

    position_size = calculate_position_size(
        PositionSizeRequest(
            account_balance=account_balance,
            risk_percent=risk_percent,
            stop_loss_points=stop_loss_points,
            asset=context.asset,
        )
    )

    stop_loss_distance = (
        stop_loss_points * context.asset.point_size
    )

    take_profit_distance = (
        take_profit_points * context.asset.point_size
    )

    if direction == "BUY":

        stop_loss = (
            entry_price - stop_loss_distance
        )

        take_profit = (
            entry_price + take_profit_distance
        )

    elif direction == "SELL":

        stop_loss = (
            entry_price + stop_loss_distance
        )

        take_profit = (
            entry_price - take_profit_distance
        )

    else:
        raise ValueError(
            f"Unsupported direction: {direction}"
        )

    return TradePlan(
        symbol=context.asset.symbol,
        timeframe=context.timeframe,
        direction=direction,
        entry_price=entry_price,
        stop_loss=stop_loss,
        take_profit=take_profit,
        risk_percent=risk_percent,
        position_size=position_size,
    )
