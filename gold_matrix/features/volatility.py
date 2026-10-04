from data.market_series import MarketDataSeries


def detect_volatility(
    series: MarketDataSeries,
) -> str:

    if len(series) < 2:
        return "NORMAL"

    previous_range = (
        series.data[-2].high
        - series.data[-2].low
    )

    latest_range = (
        series.data[-1].high
        - series.data[-1].low
    )

    if latest_range > previous_range:
        return "HIGH"

    if latest_range < previous_range:
        return "LOW"

    return "NORMAL"
