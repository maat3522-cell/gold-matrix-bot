from rules import run_rules


def main():
    print("RULES TEST")
    print("-------------------")

    bullish = run_rules(
        "BULLISH",
        "STRONG",
        "NORMAL",
    )

    bearish = run_rules(
        "BEARISH",
        "STRONG",
        "NORMAL",
    )

    neutral = run_rules(
        "NEUTRAL",
        "NEUTRAL",
        "NORMAL",
    )

    print("Bullish:")
    print(bullish)

    print()
    print("Bearish:")
    print(bearish)

    print()
    print("Neutral:")
    print(neutral)

    assert bullish["trend"]["score"] == 40
    assert bullish["momentum"]["score"] == 30
    assert bullish["volatility"]["score"] == 10

    assert bearish["trend"]["score"] == -40
    assert bearish["momentum"]["score"] == -30
    assert bearish["volatility"]["score"] == 10

    assert neutral["trend"]["score"] == 0
    assert neutral["momentum"]["score"] == 0
    assert neutral["volatility"]["score"] == 10

    print()
    print("ALL RULE TESTS PASSED")


if __name__ == "__main__":
    main()
