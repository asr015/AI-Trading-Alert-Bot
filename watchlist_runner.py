from watchlist import WATCHLIST
from scanner import get_stock_data
from scanner_engine import calculate_score
from signal_engine import generate_signal

def run_watchlist():

    results = []

    for symbol in WATCHLIST:

        try:

            data = get_stock_data(symbol)

            if data.empty:
                continue

            score = calculate_score(data)

            signal = generate_signal(score)

            results.append({
                "symbol": symbol,
                "score": score,
                "signal": signal["signal"],
                "confidence": signal["confidence"]
            })

        except Exception as e:
            print(f"{symbol} : {e}")

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:3]
