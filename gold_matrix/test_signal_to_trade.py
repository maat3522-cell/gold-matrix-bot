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

    # BUY SIGNAL
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
        signal_id="SIG-TEST-BUY-001",
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
    print(f"Signal ID: {buy_signal.signal_id}")
    print(f"Strategy: {buy_signal.strategy}")
    print(f"Entry: {buy_plan.entry_price}")
    print(f"SL: {buy_plan.stop_loss}")
    print(f"TP: {buy_plan.take_profit}")
    print(f"Size: {buy_plan.position_size}")
    print(f"Trade ID: {buy_plan.trade_id}")
    print(f"Trade Plan Signal ID: {buy_plan.signal_id}")
    print(f"Trade Plan Strategy: {buy_plan.strategy}")

    assert buy_plan.direction == "BUY"
    assert buy_plan.entry_price == 4430
    assert buy_plan.stop_loss == 4429
    assert buy_plan.take_profit == 4432
    assert buy_plan.position_size == 1.0
    assert buy_plan.strategy == "default"
    assert buy_plan.signal_id == "SIG-TEST-BUY-001"
    assert buy_plan.trade_id is not None
    assert buy_plan.trade_id.startswith("TRD-")
    assert len(buy_plan.trade_id) == 16

    print("BUY SIGNAL: PASSED")

    print()

    # SELL SIGNAL
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
        signal_id="SIG-TEST-SELL-001",
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
    print(f"Signal ID: {sell_signal.signal_id}")
    print(f"Strategy: {sell_signal.strategy}")
    print(f"Entry: {sell_plan.entry_price}")
    print(f"SL: {sell_plan.stop_loss}")
    print(f"TP: {sell_plan.take_profit}")
    print(f"Size: {sell_plan.position_size}")
    print(f"Trade ID: {sell_plan.trade_id}")
    print(f"Trade Plan Signal ID: {sell_plan.signal_id}")
    print(f"Trade Plan Strategy: {sell_plan.strategy}")

    assert sell_plan.direction == "SELL"
    assert sell_plan.entry_price == 4430
    assert sell_plan.stop_loss == 4431
    assert sell_plan.take_profit == 4428
    assert sell_plan.position_size == 1.0
    assert sell_plan.strategy == "default"
    assert sell_plan.signal_id == "SIG-TEST-SELL-001"
    assert sell_plan.trade_id is not None
    assert sell_plan.trade_id.startswith("TRD-")
    assert len(sell_plan.trade_id) == 16

    assert buy_plan.trade_id != sell_plan.trade_id

    print("SELL SIGNAL: PASSED")
    print("TRADE ID UNIQUENESS: PASSED")

    print()

    # WAIT SIGNAL
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
        signal_id="SIG-TEST-WAIT-001",
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

    # SYMBOL MISMATCH
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
        signal_id="SIG-TEST-WRONG-SYMBOL",
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

    # ASSET TYPE MISMATCH
    print("Testing asset type mismatch...")

    wrong_asset_type_signal = Signal(
        symbol="XAUUSD",
        asset_type="forex",
        timeframe="M5",
        signal="BUY",
        price=4430,
        score=80,
        confidence=80,
        reason="Bullish conditions detected",
        strategy="default",
        signal_id="SIG-TEST-WRONG-ASSET-TYPE",
    )

    try:
        build_trade_plan_from_signal(
            signal=wrong_asset_type_signal,
            context=context,
            account_balance=10000,
            risk_percent=1.0,
            stop_loss_points=100,
            take_profit_points=200,
            risk_manager=risk_manager,
        )

        raise AssertionError(
            "Asset type mismatch should fail"
        )

    except ValueError:
        pass

    print("Asset type validation: PASSED")

    print()
    print("ALL SIGNAL TO TRADE TESTS PASSED")


if __name__ == "__main__":
    main()
