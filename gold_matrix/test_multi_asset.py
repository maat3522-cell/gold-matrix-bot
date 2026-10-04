from math import isclose

from asset_registry import get_asset
from market import MarketContext
from risk_manager import RiskLimits, RiskManager
from trade_planner import build_trade_plan


def main():
    print("MULTI ASSET TEST")
    print("-------------------")

    risk_manager = RiskManager(
        RiskLimits(
            max_risk_percent=1.0,
            max_daily_loss_percent=3.0,
            max_open_positions=3,
        )
    )

    # XAUUSD
    xau = get_asset("XAUUSD")

    xau_context = MarketContext(
        asset=xau,
        timeframe="M5",
        price=4430,
    )

    xau_plan = build_trade_plan(
        context=xau_context,
        direction="BUY",
        entry_price=4430,
        stop_loss_points=100,
        take_profit_points=200,
        account_balance=10000,
        risk_percent=1.0,
        risk_manager=risk_manager,
    )

    print("XAUUSD")
    print(f"Entry: {xau_plan.entry_price}")
    print(f"SL: {xau_plan.stop_loss}")
    print(f"TP: {xau_plan.take_profit}")
    print(f"Size: {xau_plan.position_size}")

    assert isclose(
        xau_plan.stop_loss,
        4429,
        rel_tol=0,
        abs_tol=1e-9,
    )

    assert isclose(
        xau_plan.take_profit,
        4432,
        rel_tol=0,
        abs_tol=1e-9,
    )

    assert isclose(
        xau_plan.position_size,
        1.0,
        rel_tol=0,
        abs_tol=1e-9,
    )

    print()

    # EURUSD
    eur = get_asset("EURUSD")

    eur_context = MarketContext(
        asset=eur,
        timeframe="M5",
        price=1.10000,
    )

    eur_plan = build_trade_plan(
        context=eur_context,
        direction="BUY",
        entry_price=1.10000,
        stop_loss_points=100,
        take_profit_points=200,
        account_balance=10000,
        risk_percent=1.0,
        risk_manager=risk_manager,
    )

    print("EURUSD")
    print(f"Entry: {eur_plan.entry_price}")
    print(f"SL: {eur_plan.stop_loss}")
    print(f"TP: {eur_plan.take_profit}")
    print(f"Size: {eur_plan.position_size}")

    assert isclose(
        eur_plan.stop_loss,
        1.099,
        rel_tol=0,
        abs_tol=1e-9,
    )

    assert isclose(
        eur_plan.take_profit,
        1.102,
        rel_tol=0,
        abs_tol=1e-9,
    )

    assert isclose(
        eur_plan.position_size,
        1.0,
        rel_tol=0,
        abs_tol=1e-9,
    )

    print()
    print("XAUUSD: PASSED")
    print("EURUSD: PASSED")
    print()
    print("ALL MULTI ASSET TESTS PASSED")


if __name__ == "__main__":
    main()
