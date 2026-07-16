# ==========================================
# TradingASR AI Pro v3.0
# File : index_engine.py
# Part 1 / 3
# ==========================================

import pandas as pd
import yfinance as yf

from indicator_engine import calculate_indicators
from risk_engine import calculate_trade


# ==========================================
# INDEX SYMBOLS
# ==========================================

INDEXES = {
    "NIFTY": "^NSEI",
    "BANKNIFTY": "^NSEBANK"
}


# ==========================================
# DOWNLOAD INDEX DATA
# ==========================================

def get_index_data(symbol):

    try:

        df = yf.download(
            symbol,
            period="6mo",
            interval="1d",
            auto_adjust=True,
            progress=False,
            threads=False,
            timeout=30
        )

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df is None or df.empty:
            return pd.DataFrame()

        df = df.dropna()

        return df

    except Exception as e:

        print(f"{symbol} : {e}")

        return pd.DataFrame()


# ==========================================
# ANALYZE SINGLE INDEX
# ==========================================

def analyze_index(name, symbol):

    data = get_index_data(symbol)

    if data.empty:

        return {
            "index": name,
            "signal": "NO DATA",
            "score": 0,
            "confidence": "0%",
            "reasons": [
                "Unable to download index data"
            ]
        }

    df = calculate_indicators(data)

    if len(df) < 30:

        return {
            "index": name,
            "signal": "NO DATA",
            "score": 0,
            "confidence": "0%",
            "reasons": [
                "Not enough historical candles"
            ]
        }

    last = df.iloc[-1]
    prev = df.iloc[-2]

    score = 0
    reasons = []
        # ==========================================
    # EMA
    # ==========================================

    if last["EMA20"] > last["EMA50"]:
        score += 30
        reasons.append("✅ EMA20 > EMA50")
    else:
        score -= 30
        reasons.append("🔴 EMA20 < EMA50")

    if last["EMA50"] > last["EMA200"]:
        score += 30
        reasons.append("✅ Above EMA200")
    else:
        score -= 30
        reasons.append("🔴 Below EMA200")

    # ==========================================
    # RSI
    # ==========================================

    if last["RSI"] >= 60:
        score += 25
        reasons.append("✅ Strong RSI")

    elif last["RSI"] <= 40:
        score -= 25
        reasons.append("🔴 Weak RSI")

    # ==========================================
    # MACD
    # ==========================================

    if last["MACD"] > last["Signal"]:
        score += 25
        reasons.append("✅ MACD Bullish")
    else:
        score -= 25
        reasons.append("🔴 MACD Bearish")

    # ==========================================
    # VWAP
    # ==========================================

    if last["Close"] > last["VWAP"]:
        score += 20
        reasons.append("✅ Above VWAP")
    else:
        score -= 20
        reasons.append("🔴 Below VWAP")

    # ==========================================
    # Relative Volume
    # ==========================================

    if last["RVOL"] >= 1.5:
        score += 20
        reasons.append("✅ High Relative Volume")

    # ==========================================
    # Trend Strength
    # ==========================================

    if last["EMA20"] > prev["EMA20"]:
        score += 20
        reasons.append("📈 Rising Trend")
    else:
        score -= 20
        reasons.append("📉 Falling Trend")

    # ==========================================
    # ATR Based Trade
    # ==========================================

    trade = calculate_trade(df, score)

    # ==========================================
    # SCORE LIMIT
    # ==========================================

    score = max(min(score, 300), -300)

    # ==========================================
    # CONFIDENCE
    # ==========================================

    if score >= 220:
        signal = "🔥 HIGH PROBABILITY BUY"
        confidence = "95%"

    elif score >= 150:
        signal = "🟢 BUY"
        confidence = "85%"

    elif score <= -220:
        signal = "🔥 HIGH PROBABILITY SELL"
        confidence = "95%"

    elif score <= -150:
        signal = "🔴 SELL"
        confidence = "85%"

    else:
        signal = "🟡 WAIT"
        confidence = "60%"
            # ==========================================
    # REMOVE DUPLICATE REASONS
    # ==========================================

    reasons = list(dict.fromkeys(reasons))

    # ==========================================
    # FINAL RESULT
    # ==========================================

    return {

        "index": name,

        "signal": signal,

        "score": score,

        "confidence": confidence,

        "entry": trade["entry"],

        "sl": trade["sl"],

        "target1": trade["target1"],

        "target2": trade["target2"],

        "reasons": reasons

    }


# ==========================================
# RUN INDEX ENGINE
# ==========================================

def run_index_engine():

    results = []

    for name, symbol in INDEXES.items():

        result = analyze_index(name, symbol)

        results.append(result)

    return results


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    indexes = run_index_engine()

    for item in indexes:

        print("=" * 50)

        print(item["index"])

        print(item["signal"])

        print(f"Score : {item['score']}")

        print(f"Confidence : {item['confidence']}")

        print(f"Entry : {item['entry']}")

        print(f"SL : {item['sl']}")

        print(f"T1 : {item['target1']}")

        print(f"T2 : {item['target2']}")

        print("Reasons:")

        for reason in item["reasons"]:

            print(reason)

        print("=" * 50)
        
