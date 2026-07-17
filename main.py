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
