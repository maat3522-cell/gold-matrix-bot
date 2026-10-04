from data.market_series import MarketDataSeries


def detect_trend(
    series: MarketDataSeries,
) -> str:

    if len(series) < 2:
        return "NEUTRAL"

    previous_close = series.data[-2].close
    latest_close = series.data[-1].close

    if latest_close > previous_close:
        return "BULLISH"

    if latest_close < previous_close:
        return "BEARISH"

    return "NEUTRAL"
