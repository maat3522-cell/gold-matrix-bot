from data.market_series import MarketDataSeries


def detect_volatility(
    series: MarketDataSeries,
) -> str:

    if len(series) < 6:
        return "NORMAL"

    ranges = []

    for candle in series.data[-6:]:
        candle_range = (
            candle.high - candle.low
        )

        ranges.append(candle_range)

    average_range = (
        sum(ranges[:-1])
        / len(ranges[:-1])
    )

    latest_range = ranges[-1]

    if latest_range > average_range * 1.5:
        return "HIGH"

    if latest_range < average_range * 0.7:
        return "LOW"

    return "NORMAL"
