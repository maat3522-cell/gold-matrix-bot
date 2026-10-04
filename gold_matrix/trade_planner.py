from market import MarketContext
from trade_plan import TradePlan
from risk_manager import RiskManager
from position_sizing import (
    PositionSizeRequest,
    calculate_position_size,
)
from price_utils import (
    normalize_price,
    points_to_price_distance,
)
from trade_plan_validator import validate_trade_plan


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

    if stop_loss_points <= 0:
        raise ValueError(
            "Stop loss points must be greater than zero."
        )

    if take_profit_points <= 0:
        raise ValueError(
            "Take profit points must be greater than zero."
        )

    entry_price = normalize_price(
        entry_price,
        context.asset,
    )

    position_size = calculate_position_size(
        PositionSizeRequest(
            account_balance=account_balance,
            risk_percent=risk_percent,
            stop_loss_points=stop_loss_points,
            asset=context.asset,
        )
    )

    stop_loss_distance = points_to_price_distance(
        stop_loss_points,
        context.asset,
    )

    take_profit_distance = points_to_price_distance(
        take_profit_points,
        context.asset,
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

    stop_loss = normalize_price(
        stop_loss,
        context.asset,
    )

    take_profit = normalize_price(
        take_profit,
        context.asset,
    )

    plan = TradePlan(
        symbol=context.asset.symbol,
        timeframe=context.timeframe,
        direction=direction,
        entry_price=entry_price,
        stop_loss=stop_loss,
        take_profit=take_profit,
        risk_percent=risk_percent,
        position_size=position_size,
    )

    if not validate_trade_plan(plan):
        raise ValueError(
            "Generated trade plan is invalid."
        )

    return plan
