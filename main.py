# ==========================================
# TradingASR AI Pro v4.0
# File : main.py
# ==========================================

from watchlist_runner import run_watchlist
import traceback
import time
import sys


def main():

    print("=" * 60)
    print("🚀 TradingASR AI Pro v4.0")
    print("=" * 60)

    start = time.time()

    result = None

    try:

        result = run_watchlist()

        print("\n✅ Scan Completed Successfully")

    except Exception:

        print("\n❌ Fatal Error\n")

        traceback.print_exc()

    finally:

        end = time.time()

        execution_time = round(end - start, 2)

        print("\n" + "=" * 60)
        print("📊 EXECUTION SUMMARY")
        print("=" * 60)

        print(f"⏱ Execution Time : {execution_time} sec")

        if result:

            summary = result.get("summary", {})

            print(f"📈 Stocks Scanned : {summary.get('scanned', 0)}")
            print(f"🟢 Bullish : {summary.get('bullish', 0)}")
            print(f"🔴 Bearish : {summary.get('bearish', 0)}")
            print(f"🟡 Neutral : {summary.get('neutral', 0)}")
            print(f"🏆 High Probability Trades : {len(result.get('trades', []))}")

        print("=" * 60)

    return result


if __name__ == "__main__":

    result = main()

    if result is None:
        sys.exit(1)

    sys.exit(0)
