# ==========================================
# TradingASR AI Pro v2.1
# File : watchlist_runner.py
# ==========================================

from master_ai_engine import final_ai_score
from dynamic_watchlist import get_watchlist
from scanner import get_stock_data
from scanner_engine import calculate_score


def run_watchlist():

    results = []

    watchlist = get_watchlist()

    total = len(watchlist)

    print(f"Scanning {total} F&O Stocks...")

    for i, symbol in enumerate(watchlist, start=1):

        print(f"[{i}/{total}] {symbol}")

        try:

            data = get_stock_data(symbol)

            if data is None or data.empty:
                continue

            analysis = calculate_score(data)

            decision = final_ai_score(
                symbol,
                analysis["score"]
            )

            results.append({

                "symbol": symbol,

                "score": decision.get("score", 0),

                "reasons": analysis.get("reasons", []),

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

    results.sort(
        key=lambda x: abs(x["score"]),
        reverse=True
    )

    filtered = [
        stock
        for stock in results
        if abs(stock["score"]) >= 150
    ]

    if not filtered:
        filtered = results[:5]

    return filtered
