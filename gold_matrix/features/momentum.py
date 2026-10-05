from data.market_series import MarketDataSeries


def detect_momentum(
    series: MarketDataSeries,
) -> str:

    if len(series) < 3:
        return "NEUTRAL"

    previous_close = series.data[-2].close
    latest_close = series.data[-1].close
    before_previous_close = series.data[-3].close

    latest_change = latest_close - previous_close
    previous_change = previous_close - before_previous_close

    if (
        latest_change > 0
        and previous_change > 0
    ):
        return "STRONG"

    if (
        latest_change < 0
        and previous_change < 0
    ):
        return "STRONG"

    return "NEUTRAL"
