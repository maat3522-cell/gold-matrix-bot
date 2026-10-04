from data.market_series import MarketDataSeries


def detect_momentum(
    series: MarketDataSeries,
) -> str:

    if len(series) < 2:
        return "NEUTRAL"

    previous_close = series.data[-2].close
    latest_close = series.data[-1].close

    change = latest_close - previous_close

    if change > 0:
        return "STRONG"

    if change < 0:
        return "STRONG"

    return "NEUTRAL"
