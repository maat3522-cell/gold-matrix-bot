from backtest_result import BacktestTrade

from backtest.metrics import (
    calculate_average_profit,
    calculate_average_loss,
    calculate_largest_win,
    calculate_largest_loss,
    calculate_profit_factor,
    calculate_max_drawdown,
)


def main():
    print("BACKTEST METRICS TEST")
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
            direction="BUY",
            entry_price=4440.0,
            exit_price=4455.0,
            profit_loss=15.0,
        ),
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="SELL",
            entry_price=4455.0,
            exit_price=4463.0,
            profit_loss=-8.0,
        ),
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="SELL",
            entry_price=4463.0,
            exit_price=4470.0,
            profit_loss=-7.0,
        ),
        BacktestTrade(
            symbol="XAUUSD",
            timeframe="M5",
            direction="BUY",
            entry_price=4470.0,
            exit_price=4482.0,
            profit_loss=12.0,
        ),
    ]

    average_profit = calculate_average_profit(trades)
    average_loss = calculate_average_loss(trades)
    largest_win = calculate_largest_win(trades)
    largest_loss = calculate_largest_loss(trades)
    profit_factor = calculate_profit_factor(trades)
    max_drawdown = calculate_max_drawdown(trades)

    print(f"Average profit: {average_profit}")
    print(f"Average loss: {average_loss}")
    print(f"Largest win: {largest_win}")
    print(f"Largest loss: {largest_loss}")
    print(f"Profit factor: {profit_factor}")
    print(f"Max drawdown: {max_drawdown}")

    assert average_profit == 12.333333333333334
    assert average_loss == -7.5
    assert largest_win == 15.0
    assert largest_loss == -8.0

    assert profit_factor == 37.0 / 15.0
    assert max_drawdown == 15.0

    print()
    print("AVERAGE PROFIT: PASSED")
    print("AVERAGE LOSS: PASSED")
    print("LARGEST WIN: PASSED")
    print("LARGEST LOSS: PASSED")
    print("PROFIT FACTOR: PASSED")
    print("MAX DRAWDOWN: PASSED")

    print()
    print("ALL BACKTEST METRICS TESTS PASSED")


if __name__ == "__main__":
    main()
