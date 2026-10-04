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
    point_value: float,
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
            point_value=point_value,
        )
    )

    if direction == "BUY":
        stop_loss = (
            entry_price - stop_loss_points
        )
        take_profit = (
            entry_price + take_profit_points
        )

    elif direction == "SELL":
        stop_loss = (
            entry_price + stop_loss_points
        )
        take_profit = (
            entry_price - take_profit_points
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
    )
