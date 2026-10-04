from signal import Signal

from asset_registry import get_asset
from market import MarketContext
from risk_manager import RiskLimits, RiskManager
from signal_to_trade import build_trade_plan_from_signal


def main():
    print("SIGNAL TO TRADE TEST")
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

    # =========================
    # BUY SIGNAL
    # =========================

    buy_signal = Signal(
        symbol="XAUUSD",
        asset_type="metal",
        timeframe="M5",
        signal="BUY",
        price=4430,
        score=80,
        confidence=80,
        reason="Bullish conditions detected",
        strategy="default",
    )

    buy_plan = build_trade_plan_from_signal(
        signal=buy_signal,
        context=context,
        account_balance=10000,
        risk_percent=1.0,
        stop_loss_points=100,
        take_profit_points=200,
        risk_manager=risk_manager,
    )

    print("BUY SIGNAL")
    print(f"Signal: {buy_signal.signal}")
    print(f"Entry: {buy_plan.entry_price}")
    print(f"SL: {buy_plan.stop_loss}")
    print(f"TP: {buy_plan.take_profit}")
    print(f"Size: {buy_plan.position_size}")

    assert buy_plan.direction == "BUY"
    assert buy_plan.entry_price == 4430
    assert buy_plan.stop_loss == 4429
    assert buy_plan.take_profit == 4432
    assert buy_plan.position_size == 1.0

    print("BUY SIGNAL: PASSED")

    print()

    # =========================
    # SELL SIGNAL
    # =========================

    sell_signal = Signal(
        symbol="XAUUSD",
        asset_type="metal",
        timeframe="M5",
        signal="SELL",
        price=4430,
        score=-70,
        confidence=70,
        reason="Bearish conditions detected",
        strategy="default",
    )

    sell_plan = build_trade_plan_from_signal(
        signal=sell_signal,
        context=context,
        account_balance=10000,
        risk_percent=1.0,
        stop_loss_points=100,
        take_profit_points=200,
        risk_manager=risk_manager,
    )

    print("SELL SIGNAL")
    print(f"Signal: {sell_signal.signal}")
    print(f"Entry: {sell_plan.entry_price}")
    print(f"SL: {sell_plan.stop_loss}")
    print(f"TP: {sell_plan.take_profit}")
    print(f"Size: {sell_plan.position_size}")

    assert sell_plan.direction == "SELL"
    assert sell_plan.entry_price == 4430
    assert sell_plan.stop_loss == 4431
    assert sell_plan.take_profit == 4428
    assert sell_plan.position_size == 1.0

    print("SELL SIGNAL: PASSED")

    print()
    print("Testing WAIT signal...")

    wait_signal = Signal(
        symbol="XAUUSD",
        asset_type="metal",
        timeframe="M5",
        signal="WAIT",
        price=4430,
        score=20,
        confidence=0,
        reason="No valid setup detected",
        strategy="default",
    )

    try:
        build_trade_plan_from_signal(
            signal=wait_signal,
            context=context,
            account_balance=10000,
            risk_percent=1.0,
            stop_loss_points=100,
            take_profit_points=200,
            risk_manager=risk_manager,
        )

        raise AssertionError(
            "WAIT signal should not create a trade plan"
        )

    except ValueError:
        pass

    print("WAIT signal validation: PASSED")

    print()
    print("Testing symbol mismatch...")

    wrong_symbol_signal = Signal(
        symbol="EURUSD",
        asset_type="forex",
        timeframe="M5",
        signal="BUY",
        price=1.10000,
        score=80,
        confidence=80,
        reason="Bullish conditions detected",
        strategy="default",
    )

    try:
        build_trade_plan_from_signal(
            signal=wrong_symbol_signal,
            context=context,
            account_balance=10000,
            risk_percent=1.0,
            stop_loss_points=100,
            take_profit_points=200,
            risk_manager=risk_manager,
        )

        raise AssertionError(
            "Symbol mismatch should fail"
        )

    except ValueError:
        pass

    print("Symbol validation: PASSED")

    print()
    print("ALL SIGNAL TO TRADE TESTS PASSED")


if __name__ == "__main__":
    main()
