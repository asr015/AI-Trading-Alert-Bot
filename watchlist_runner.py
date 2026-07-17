# ==========================================
# TradingASR AI Pro v4.0
# File : watchlist_runner.py
# Part 1 / 5
# ==========================================

from scanner import get_stock_data
from dynamic_watchlist import get_watchlist

from scanner_engine import calculate_score
from master_ai_engine import (
    final_ai_score,
    set_option_chain
)

from option_chain import analyze_option_chain
from market_summary import create_summary

from index_engine import analyze_indices

from telegram_bot import send_ai_report


# ==========================================
# WATCHLIST RUNNER
# ==========================================

def run_watchlist():

    trades = []

    scanned = 0

    bullish = 0

    bearish = 0

    neutral = 0

    print("\nFetching Option Chain...")

    option_chain = analyze_option_chain()

    set_option_chain(option_chain)

    print("Option Chain Loaded")

    print("\nScanning Watchlist...\n")

    watchlist = get_watchlist()
    # ==========================================
    # STOCK SCAN LOOP
    # ==========================================

    for symbol in watchlist:

        try:

            print(f"Scanning : {symbol}")

            data = get_stock_data(symbol)

            if data is None or len(data) < 30:

                print(f"{symbol} : No Data")

                continue

            scanned += 1

            # ==================================
            # TECHNICAL SCANNER
            # ==================================

            analysis = calculate_score(data)

            # ==================================
            # MASTER AI ENGINE
            # ==================================

            decision = final_ai_score(

                symbol,

                analysis["score"]

            )

            # ==================================
            # MARKET SUMMARY
            # ==================================

            verdict = decision["verdict"]

            if "BUY" in verdict:

                bullish += 1

            elif "SELL" in verdict:

                bearish += 1

            else:

                neutral += 1

            # ==================================
            # SAVE RESULT
            # ==================================

            trades.append({

                "symbol": symbol,

                "score": decision["score"],

                "setup": analysis.get("setup", ""),

                "verdict": verdict,

                "signal": decision.get("signal", "WAIT"),

                "confidence": decision["confidence"],

                "reasons": analysis["reasons"]
                + decision["reasons"],

                "entry": analysis["entry"],

                "sl": analysis["sl"],

                "target1": analysis["target1"],

                "target2": analysis["target2"]

            })

        except Exception as e:

            print(f"{symbol} Error : {e}")
            # ==========================================
    # FILTER HIGH PROBABILITY TRADES
    # ==========================================

    filtered_trades = []

    for trade in trades:

        score = trade.get("score", 0)

        confidence = trade.get("confidence", "0%")

        try:

            confidence = int(
                confidence.replace("%", "")
            )

        except Exception:

            confidence = 0

        setup = trade.get("setup", "")

        # ======================================
        # ELITE FILTER
        # ======================================

        if (

            abs(score) >= 250

            and confidence >= 90

            and (
                "⭐⭐⭐⭐" in setup
                or
                "⭐⭐⭐⭐⭐" in setup
            )

        ):

            filtered_trades.append(trade)

    # ==========================================
    # SORT BEST TRADES
    # ==========================================

    filtered_trades = sorted(

        filtered_trades,

        key=lambda x: abs(x["score"]),

        reverse=True

    )

    # Only Best Trades
    filtered_trades = filtered_trades[:5]

    print(
        f"\nHigh Probability Trades : "
        f"{len(filtered_trades)}"
    )

    # ==========================================
    # MARKET SUMMARY
    # ==========================================

    summary = create_summary({

        "scanned": scanned,

        "bullish": bullish,

        "bearish": bearish,

        "neutral": neutral

    })
