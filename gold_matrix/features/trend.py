from data.market_series import MarketDataSeries


def detect_trend(
    series: MarketDataSeries,
) -> str:

    if len(series) < 6:
        return "NEUTRAL"

    closes = [
        candle.close
        for candle in series.data[-6:]
    ]

    rising = 0
    falling = 0

    for i in range(1, len(closes)):
        if closes[i] > closes[i - 1]:
            rising += 1
        elif closes[i] < closes[i - 1]:
            falling += 1

    if rising >= 4:
        return "BULLISH"

    if falling >= 4:
        return "BEARISH"

    return "NEUTRAL"
