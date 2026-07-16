# ==========================================
# TradingASR AI Pro v4.0
# File : scanner_engine.py
# Part 1 / 6
# ==========================================

from config import *

from indicator_engine import calculate_indicators
from smart_money_engine import smart_money_score
from liquidity_engine import liquidity_score
from structure_engine import structure_score
from order_block_engine import order_block_score
from fvg_engine import fvg_score
from news_engine import news_score
from risk_engine import calculate_trade


# ==========================================
# AI TECHNICAL SCORE
# ==========================================

def calculate_score(data):

    df = calculate_indicators(data)

    if df is None or len(df) < 30:

        return {

            "score": 0,

            "setup": "⭐ Ignore",

            "reasons": [

                "⚠️ Not enough historical data"

            ],

            "entry": 0,

            "sl": 0,

            "target1": 0,

            "target2": 0

        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0

    reasons = []

    confirmations = 0
