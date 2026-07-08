from watchlist import WATCHLIST
from scanner import get_stock_data
from scanner_engine import calculate_score

def run_watchlist():

    results = []

    for symbol in WATCHLIST:

        try:

            data = get_stock_data(symbol)

            score = calculate_score(data)

            results.append({
                "symbol": symbol,
                "score": score
            })

        except Exception as e:

            print(f"{symbol} Error : {e}")

    results = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )

    return results
