from market import MarketContext
from rules import run_rules


def calculate_score(context: MarketContext):
    rule_results = run_rules(
        context.trend,
        context.momentum,
        context.volatility,
    )

    total_score = sum(
        rule["score"]
        for rule in rule_results.values()
    )

    return total_score, rule_results
