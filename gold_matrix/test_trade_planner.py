from asset_registry import get_asset
from market import MarketContext
from risk_manager import RiskLimits, RiskManager
from trade_planner import build_trade_plan


def main():
    print("TRADE PLANNER TEST")
    print("-------------------")

    asset = get_asset("XAUUSD")

    context = MarketContext(
        asset=asset,
        timeframe="M5",
        price=4430,
        trend="BULLISH",
        momentum="STRONG",
        volatility="NORMAL",
    )

    risk_manager = RiskManager(
        RiskLimits(
            max_risk_percent=1.0,
            max_daily_loss_percent=3.0,
            max_open_positions=3,
        )
    )

    buy_plan = build_trade_plan(
        context=context,
        direction="BUY",
        entry_price=4430,
        stop_loss_points=100,
        take_profit_points=200,
        account_balance=10000,
        risk_percent=1.0,
        risk_manager=risk_manager,
    )

    sell_plan = build_trade_plan(
        context=context,
        direction="SELL",
        entry_price=4430,
        stop_loss_points=100,
        take_profit_points=200,
        account_balance=10000,
        risk_percent=1.0,
        risk_manager=risk_manager,
    )

    print("BUY PLAN")
    print(f"Entry: {buy_plan.entry_price}")
    print(f"SL: {buy_plan.stop_loss}")
    print(f"TP: {buy_plan.take_profit}")
    print(f"Position Size: {buy_plan.position_size}")

    print()
    print("SELL PLAN")
    print(f"Entry: {sell_plan.entry_price}")
    print(f"SL: {sell_plan.stop_loss}")
    print(f"TP: {sell_plan.take_profit}")
    print(f"Position Size: {sell_plan.position_size}")

    assert buy_plan.direction == "BUY"
    assert buy_plan.entry_price == 4430
    assert buy_plan.stop_loss == 4429
    assert buy_plan.take_profit == 4432
    assert buy_plan.position_size == 1.0

    assert sell_plan.direction == "SELL"
    assert sell_plan.entry_price == 4430
    assert sell_plan.stop_loss == 4431
    assert sell_plan.take_profit == 4428
    assert sell_plan.position_size == 1.0

    print()
    print("Testing invalid risk...")

    try:
        build_trade_plan(
            context=context,
            direction="BUY",
            entry_price=4430,
            stop_loss_points=100,
            take_profit_points=200,
            account_balance=10000,
            risk_percent=2.0,
            risk_manager=risk_manager,
        )

        raise AssertionError(
            "Risk above the limit should fail"
        )

    except ValueError:
        pass

    print("Risk validation: PASSED")

    print()
    print("ALL TRADE PLANNER TESTS PASSED")


if __name__ == "__main__":
    main()
