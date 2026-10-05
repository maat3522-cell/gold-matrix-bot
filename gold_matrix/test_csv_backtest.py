```python
from data.csv_loader import load_csv_market_data

from assets import get_asset

from strategy import DefaultStrategy

from backtest.config import BacktestConfig

from backtest.strategy_runner import (
    run_feature_backtest,
)


def main():

    print("CSV GOLD BACKTEST")
    print("--------------------")

    file_path = (
        "gold_matrix/data/XAUUSD_5m.csv"
    )

    series = load_csv_market_data(
        file_path
    )

    print(
        f"Loaded candles: "
        f"{len(series.data)}"
    )

    asset = get_asset("XAUUSD")

    strategy = DefaultStrategy(
        min_confidence=70
    )

    config = BacktestConfig(
        initial_balance=10000.0,
        commission_per_trade=1.0,
        slippage_per_trade=1.0,
        stop_loss_points=150.0,
        take_profit_points=300.0,
    )

    result = run_feature_backtest(
        series=series,
        symbol="XAUUSD",
        timeframe="M5",
        asset=asset,
        strategy=strategy,
        config=config,
    )

    print()
    print("RESULT")
    print("--------------------")

    print(
        f"Total trades: "
        f"{result.total_trades}"
    )

    print(
        f"Winning trades: "
        f"{result.winning_trades}"
    )

    print(
        f"Losing trades: "
        f"{result.losing_trades}"
    )

    print(
        f"Total P/L: "
        f"{result.total_profit_loss}"
    )

    print(
        f"Win rate: "
        f"{result.win_rate}%"
    )

    print(
        f"Profit factor: "
        f"{result.profit_factor}"
    )

    print(
        f"Max drawdown: "
        f"{result.max_drawdown}"
    )

    print(
        f"Initial balance: "
        f"{result.initial_balance}"
    )

    print(
        f"Final balance: "
        f"{result.final_balance}"
    )

    print()
    print("CSV BACKTEST COMPLETED")


if __name__ == "__main__":
    main()
```
