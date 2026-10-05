from data.csv_loader import load_csv_market_data
from assets import AssetProfile
from strategy import DefaultStrategy
from backtest.config import BacktestConfig
from backtest.strategy_runner import run_feature_backtest


def main():

    print("CSV GOLD BACKTEST")
    print("--------------------")

    file_path = "gold_matrix/data/XAUUSD_5m.csv"

    series = load_csv_market_data(file_path)

    print(f"Loaded candles: {len(series.data)}")

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

    buy_trades = [
        trade for trade in result.trades
        if trade.direction == "BUY"
    ]

    sell_trades = [
        trade for trade in result.trades
        if trade.direction == "SELL"
    ]

    buy_wins = [
        trade for trade in buy_trades
        if trade.profit_loss > 0
    ]

    sell_wins = [
        trade for trade in sell_trades
        if trade.profit_loss > 0
    ]

    tp_trades = [
        trade for trade in result.trades
        if trade.exit_reason == "TP"
    ]

    sl_trades = [
        trade for trade in result.trades
        if trade.exit_reason == "SL"
    ]

    print()
    print("RESULT")
    print("--------------------")

    print(f"Total trades: {result.total_trades}")
    print(f"Winning trades: {result.winning_trades}")
    print(f"Losing trades: {result.losing_trades}")
    print(f"Total P/L: {result.total_profit_loss}")
    print(f"Win rate: {result.win_rate}%")
    print(f"Profit factor: {result.profit_factor}")
    print(f"Max drawdown: {result.max_drawdown}")
    print(f"Initial balance: {result.initial_balance}")
    print(f"Final balance: {result.final_balance}")

    print()
    print("DIRECTION")
    print("--------------------")

    print(f"BUY trades: {len(buy_trades)}")
    print(f"BUY wins: {len(buy_wins)}")

    print(f"SELL trades: {len(sell_trades)}")
    print(f"SELL wins: {len(sell_wins)}")

    print()
    print("EXIT REASONS")
    print("--------------------")

    print(f"TP: {len(tp_trades)}")
    print(f"SL: {len(sl_trades)}")

    print()
    print("CSV BACKTEST COMPLETED")


if __name__ == "__main__":
    main()
