def calculate_total_score(
    trend_score,
    momentum_score,
    volume_score,
    smart_money_score,
    option_score,
    news_score,
):

    total = (
        trend_score
        + momentum_score
        + volume_score
        + smart_money_score
        + option_score
        + news_score
    )

    return total
