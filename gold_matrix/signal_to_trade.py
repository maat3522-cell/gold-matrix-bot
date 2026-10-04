from signal import Signal

from market import MarketContext
from risk_manager import RiskManager
from trade_plan import TradePlan
from trade_planner import build_trade_plan


def build_trade_plan_from_signal(
    signal: Signal,
    context: MarketContext,
    account_balance: float,
    risk_percent: float,
    stop_loss_points: float,
    take_profit_points: float,
    risk_manager: RiskManager,
) -> TradePlan:

    if signal.signal not in (
        "BUY",
        "SELL",
    ):
        raise ValueError(
            "Signal does not contain a tradable direction."
        )

    if signal.symbol != context.asset.symbol:
        raise ValueError(
            "Signal symbol does not match market context asset."
        )

    if signal.asset_type != context.asset.asset_type:
        raise ValueError(
            "Signal asset type does not match market context asset."
        )

    if signal.timeframe != context.timeframe:
        raise ValueError(
            "Signal timeframe does not match market context timeframe."
        )

    if signal.price <= 0:
        raise ValueError(
            "Signal price must be greater than zero."
        )

    plan = build_trade_plan(
        context=context,
        direction=signal.signal,
        entry_price=signal.price,
        stop_loss_points=stop_loss_points,
        take_profit_points=take_profit_points,
        account_balance=account_balance,
        risk_percent=risk_percent,
        risk_manager=risk_manager,
    )

    return TradePlan(
        symbol=plan.symbol,
        timeframe=plan.timeframe,
        direction=plan.direction,
        entry_price=plan.entry_price,
        stop_loss=plan.stop_loss,
        take_profit=plan.take_profit,
        risk_percent=plan.risk_percent,
        position_size=plan.position_size,
        strategy=signal.strategy,
        signal_id=signal.signal_id,
    )
