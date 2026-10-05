from data.market_series import MarketDataSeries


def detect_trend(
    series: MarketDataSeries,
) -> str:

    if len(series) < 4:
        return "NEUTRAL"

    close_1 = series.data[-1].close
    close_2 = series.data[-2].close
    close_3 = series.data[-3].close
    close_4 = series.data[-4].close

    if (
        close_1 > close_2
        and close_2 > close_3
        and close_3 > close_4
    ):
        return "BULLISH"

    if (
        close_1 < close_2
        and close_2 < close_3
        and close_3 < close_4
    ):
        return "BEARISH"

    return "NEUTRAL"
