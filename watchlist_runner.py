from master_ai_engine import final_ai_score
from dynamic_watchlist import get_watchlist
from scanner import get_stock_data
from scanner_engine import calculate_score


def run_watchlist():

    results = []

    for symbol in get_watchlist():

        try:

            data = get_stock_data(symbol)

            if data.empty:
                continue

            # Technical Scanner
            analysis = calculate_score(data)

            # AI Master Decision
            decision = final_ai_score(
                symbol,
                analysis["score"]
            )

            results.append({

                "symbol": symbol,

                # Final AI Score
                "score": decision["score"],

                # Technical Reasons
                "reasons": analysis["reasons"],

                # AI Reasons
                "ai_reasons": decision["reasons"],

                "verdict": decision["verdict"],

                "confidence": decision["confidence"],

                "entry": analysis["entry"],

                "sl": analysis["sl"],

                "target1": analysis["target1"],

                "target2": analysis["target2"]

            })

        except Exception as e:

            print(f"{symbol}: {e}")

    # Highest Score First
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    # Only High Probability Trades
    filtered = []

    for stock in results:

        if stock["score"] >= 150 or stock["score"] <= -150:

            filtered.append(stock)

    # Agar High Probability Trade na mile
    if len(filtered) == 0:

        filtered = results[:5]

    return filtered
