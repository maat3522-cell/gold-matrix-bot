from backtest_result import BacktestTrade

from backtest.equity import (
    calculate_equity_curve,
    calculate_final_balance,
)


def main():
    print("BACKTEST EQUITY TEST")
    print("-------------------")

    trades = [
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="BUY",
            entry_price=4430.0,
            exit_price=4440.0,
            profit_loss=10.0,
        ),
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="SELL",
            entry_price=4440.0,
            exit_price=4435.0,
            profit_loss=5.0,
        ),
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="BUY",
            entry_price=4435.0,
            exit_price=4430.0,
            profit_loss=-5.0,
        ),
    ]

    initial_balance = 10000.0

    equity_curve = calculate_equity_curve(
        trades=trades,
        initial_balance=initial_balance,
    )

    final_balance = calculate_final_balance(
        trades=trades,
        initial_balance=initial_balance,
    )

    print(f"Initial balance: {initial_balance}")
    print(f"Equity curve: {equity_curve}")
    print(f"Final balance: {final_balance}")

    assert equity_curve == [
        10000.0,
        10010.0,
        10015.0,
        10010.0,
    ]

    assert final_balance == 10010.0

    print()
    print("EQUITY CURVE: PASSED")
    print("FINAL BALANCE: PASSED")

    print()
    print("ALL BACKTEST EQUITY TESTS PASSED")


if __name__ == "__main__":
    main()
