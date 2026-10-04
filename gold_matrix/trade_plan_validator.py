from trade_plan import TradePlan


def validate_trade_plan(
    plan: TradePlan,
) -> bool:

    if plan.entry_price <= 0:
        return False

    if plan.stop_loss is not None:
        if plan.stop_loss <= 0:
            return False

    if plan.take_profit is not None:
        if plan.take_profit <= 0:
            return False

    if plan.direction == "BUY":

        if (
            plan.stop_loss is not None
            and plan.stop_loss >= plan.entry_price
        ):
            return False

        if (
            plan.take_profit is not None
            and plan.take_profit <= plan.entry_price
        ):
            return False

    elif plan.direction == "SELL":

        if (
            plan.stop_loss is not None
            and plan.stop_loss <= plan.entry_price
        ):
            return False

        if (
            plan.take_profit is not None
            and plan.take_profit >= plan.entry_price
        ):
            return False

    else:
        return False

    if (
        plan.position_size is not None
        and plan.position_size <= 0
    ):
        return False

    return True
