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

                "confidence": decision["confidence"]

            })

        except Exception as e:

            print(f"{symbol}: {e}")

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results
