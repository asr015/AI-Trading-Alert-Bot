# ==========================================
# TradingASR AI Pro v4.0
# File : main.py
# Part 1 / 3
# ==========================================

from watchlist_runner import run_watchlist

import traceback

import time


# ==========================================
# MAIN
# ==========================================

def main():

    print("=" * 60)

    print("🚀 TradingASR AI Pro v4.0")

    print("=" * 60)

    start = time.time()

    try:

        result = run_watchlist()

        print("\n✅ Scan Completed Successfully")

        return result

    except Exception:

        print("\n❌ Fatal Error\n")

        traceback.print_exc()

        return None
            finally:

        end = time.time()

        execution_time = round(

            end - start,

            2

        )

        print("\n" + "=" * 60)

        print("📊 EXECUTION SUMMARY")

        print("=" * 60)

        print(

            f"⏱ Execution Time : "

            f"{execution_time} sec"

        )

        if result:

            summary = result.get(

                "summary",

                {}

            )

            print(

                f"📈 Stocks Scanned : "

                f"{summary.get('scanned',0)}"

            )

            print(

                f"🟢 Bullish : "

                f"{summary.get('bullish',0)}"

            )

            print(

                f"🔴 Bearish : "

                f"{summary.get('bearish',0)}"

            )

            print(

                f"🟡 Neutral : "

                f"{summary.get('neutral',0)}"

            )

            print(

                f"🏆 High Probability Trades : "

                f"{len(result.get('trades',[]))}"

            )

        print("=" * 60)
