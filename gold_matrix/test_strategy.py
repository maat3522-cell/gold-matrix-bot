from strategy import DefaultStrategy


def main():
    strategy = DefaultStrategy(min_confidence=70)

    buy = strategy.evaluate(80)
    sell = strategy.evaluate(-80)
    wait = strategy.evaluate(40)

    print("STRATEGY TEST")
    print("-------------------")

    print(f"BUY test: {buy.signal} | confidence={buy.confidence}")
    print(f"SELL test: {sell.signal} | confidence={sell.confidence}")
    print(f"WAIT test: {wait.signal} | confidence={wait.confidence}")

    assert buy.signal == "BUY"
    assert buy.confidence == 80

    assert sell.signal == "SELL"
    assert sell.confidence == 80

    assert wait.signal == "WAIT"
    assert wait.confidence == 0

    print()
    print("ALL STRATEGY TESTS PASSED")


if __name__ == "__main__":
    main()
