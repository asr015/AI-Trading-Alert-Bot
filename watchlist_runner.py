# ==========================================
# TradingASR AI Pro v2.2
# File : watchlist_runner.py
# ==========================================

from master_ai_engine import (
    final_ai_score,
    set_option_chain
)

from option_chain import analyze_option_chain
from dynamic_watchlist import get_watchlist
from scanner import get_stock_data
from scanner_engine import calculate_score


def run_watchlist():

    results = []

    # ==========================
    # Fetch Option Chain Only Once
    # ==========================

    option = analyze_option_chain()

    set_option_chain(option)

    # ==========================
    # Get Watchlist
    # ==========================

    watchlist = get_watchlist()

    total = len(watchlist)

    print(f"Scanning {total} F&O Stocks...")

    # ==========================
    # Start Scan
    # ==========================

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

                "score":
