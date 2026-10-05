from data.market_series import MarketDataSeries


def detect_momentum(series: MarketDataSeries) -> str:

    if len(series) < 4:
        return "NEUTRAL"

    close_1 = series.data[-1].close
    close_2 = series.data[-2].close
    close_3 = series.data[-3].close
    close_4 = series.data[-4].close

    move_1 = close_1 - close_2
    move_2 = close_2 - close_3
    move_3 = close_3 - close_4

    bullish_moves = (
        move_1 > 0
        and move_2 > 0
        and move_3 > 0
    )

    bearish_moves = (
        move_1 < 0
        and move_2 < 0
        and move_3 < 0
    )

    if bullish_moves:
        return "STRONG"

    if bearish_moves:
        return "STRONG"

    return "NEUTRAL"
