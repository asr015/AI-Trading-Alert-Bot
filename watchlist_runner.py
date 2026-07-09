from master_ai_engine import final_ai_score
from dynamic_watchlist import get_watchlist
from scanner import get_stock_data
from scanner_engine import calculate_score
from ai_decision_engine import analyze_setup


def run_watchlist():

    results = []

    for symbol in get_watchlist():

        try:

            data = get_stock_data(symbol)

            if data.empty:
                continue

            analysis = calculate_score(data)

            decision = analyze_setup(
                analysis["score"],
                analysis["reasons"]
            )

            results.append({

                "symbol": symbol,

                "score": analysis["score"],

                "reasons": analysis["reasons"],

                "verdict": decision["verdict"],

                "confidence": decision["confidence"],

                "entry": analysis["entry"],

                "sl": analysis["sl"],

                "target1": analysis["target1"],

                "target2": analysis["target2"]

            })

        except Exception as e:

            print(f"{symbol}: {e}")

    # Highest score first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Only High Probability Trades
    filtered = []

    for stock in results:

        if stock["score"] >= 150 or stock["score"] <= -150:

            filtered.append(stock)

    # Agar koi high probability trade na mile
    if len(filtered) == 0:

        filtered = results[:5]

    return filtered
