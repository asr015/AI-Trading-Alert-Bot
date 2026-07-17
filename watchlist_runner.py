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
