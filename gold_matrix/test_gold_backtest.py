from datetime import datetime, timedelta

from assets import AssetProfile

from backtest.strategy_runner import run_feature_backtest
from backtest.config import BacktestConfig

from data.market_data import MarketData
from data.market_series import MarketDataSeries

from strategy import DefaultStrategy


def build_sample_data():
    prices = [
        4430.0,
        4432.0,
        4435.0,
        4438.0,
        4441.0,
        4444.0,
        4442.0,
        4440.0,
        4437.0,
        4435.0,
        4438.0,
        4442.0,
        4446.0,
        4450.0,
        4453.0,
        4455.0,
        4452.0,
        4448.0,
        4445.0,
        4442.0,
        4440.0,
        4437.0,
        4435.0,
        4432.0,
        4430.0,
        4433.0,
        4436.0,
        4440.0,
        4444.0,
        4448.0,
        4452.0,
        4456.0,
        4459.0,
        4462.0,
        4458.0,
        4454.0,
        4450.0,
        4446.0,
        4442.0,
        4438.0,
    ]

    data = []

    start_time = datetime(
        2026,
        1,
        1,
        10,
        0,
    )

    for index, close in enumerate(prices):

        previous_close = (
            prices[index - 1]
            if index > 0
            else close
        )

        candle_range = 1.0

        open_price = previous_close

        high_price = max(
            open_price,
            close,
        ) + candle_range

        low_price = min(
            open_price,
            close,
        ) - candle_range

        data.append(
            MarketData(
                symbol="XAUUSD",
                timeframe="M5",
                timestamp=(
                    start_time
                    + timedelta(minutes=5 * index)
                ),
                open=open_price,
                high=high_price,
                low=low_price,
                close=close,
            )
        )

    return MarketDataSeries(data=data)


def main():

    print("GOLD MATRIX BACKTEST")
    print("--------------------")

    asset = AssetProfile(
        symbol="XAUUSD",
        asset_type="metal",
        price_decimals=2,
        point_size=0.01,
        min_volume=0.01,
        max_volume=100.0,
        volume_step=0.01,
        tick_size=0.01,
        tick_value=1.0,
    )

    strategy = DefaultStrategy(
        min_confidence=70
    )

    config = BacktestConfig(
        initial_balance=10000.0,
        commission_per_trade=1.0,
        slippage_per_trade=1.0,
        allow_long=True,
        allow_short=True,
        stop_loss_points=150.0,
        take_profit_points=300.0,
    )

    series = build_sample_data()

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

    print(f"Total trades: {result.total_trades}")
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
        f"Average profit: "
        f"{result.average_profit}"
    )
    print(
        f"Average loss: "
        f"{result.average_loss}"
    )
    print(
        f"Largest win: "
        f"{result.largest_win}"
    )
    print(
        f"Largest loss: "
        f"{result.largest_loss}"
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
    print("BACKTEST COMPLETED")


if __name__ == "__main__":
    main()
