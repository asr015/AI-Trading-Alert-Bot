from master_ai_engine import final_ai_score
from dynamic_watchlist import get_watchlist
from scanner import get_stock_data
from scanner_engine import calculate_score


def run_watchlist():

    results = []

    for symbol in get_watchlist():

        try:

            data = get_stock_data(symbol)

            # Safe Data Check
            if data is None or data.empty:
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
                "score": decision.get("score", 0),

                # Technical Reasons
                "reasons": analysis.get("reasons", []),

                # AI Reasons
                "ai_reasons": decision.get("reasons", []),

                "verdict": decision.get("verdict", "Neutral"),

                "confidence": decision.get("confidence", "Low"),

                "entry": analysis.get("entry", "N/A"),

                "sl": analysis.get("sl", "N/A"),

                "target1": analysis.get("target1", "N/A"),

                "target2": analysis.get("target2", "N/A")

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

        if abs(stock["score"]) >= 150:

            filtered.append(stock)

    # If no High Probability Trade found
    if len(filtered) == 0:

        filtered = results[:5]

    return filtered
