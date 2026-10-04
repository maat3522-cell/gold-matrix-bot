
from backtest.config import BacktestConfig
from backtest.executor import execute_backtest_trades


def main():
    print("BACKTEST EXECUTOR TEST")
    print("-------------------")

    config = BacktestConfig(
        initial_balance=10000.0,
        commission_per_trade=1.0,
        slippage_per_trade=1.0,
        allow_long=True,
        allow_short=True,
    )

    signals = {
        1: "BUY",
        2: "SELL",
        3: "BUY",
    }

    prices = {
        1: (4430.0, 4435.0),
        2: (4435.0, 4432.0),
        3: (4432.0, 4444.0),
    }

    def signal_provider(index):
        return signals.get(index)

    def price_provider(index):
        return prices[index]

    trades = execute_backtest_trades(
        total_steps=4,
        symbol="XAUUSD",
        timeframe="M5",
        config=config,
        signal_provider=signal_provider,
        price_provider=price_provider,
    )

    print(f"Total trades: {len(trades)}")

    for index, trade in enumerate(trades, start=1):

        print(
            f"Trade {index}: "
            f"{trade.direction} "
            f"{trade.entry_price} -> "
            f"{trade.exit_price} "
            f"P/L={trade.profit_loss}"
        )

    assert len(trades) == 3

    assert trades[0].direction == "BUY"
    assert trades[0].profit_loss == 3.0

    assert trades[1].direction == "SELL"
    assert trades[1].profit_loss == 1.0

    assert trades[2].direction == "BUY"
    assert trades[2].profit_loss == 10.0

    assert sum(
        trade.profit_loss
        for trade in trades
    ) == 14.0

    print()
    print("TRADE COUNT: PASSED")
    print("BUY TRADE: PASSED")
    print("SELL TRADE: PASSED")
    print("COSTS: PASSED")
    print("TOTAL P/L: PASSED")

    print()
    print("ALL BACKTEST EXECUTOR TESTS PASSED")


if __name__ == "__main__":
    main()
