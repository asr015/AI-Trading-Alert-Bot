# ==========================================
# TradingASR AI Pro v3.0
# File : relative_strength_engine.py
# ==========================================

import yfinance as yf


def relative_strength_score(symbol, df):

    score = 0
    reasons = []

    try:

        nifty = yf.download(
            "^NSEI",
            period="5d",
            interval="1d",
            progress=False
        )

        stock_return = (
            df["Close"].iloc[-1] -
            df["Close"].iloc[-5]
        ) / df["Close"].iloc[-5] * 100

        nifty_return = (
            nifty["Close"].iloc[-1] -
            nifty["Close"].iloc[-5]
        ) / nifty["Close"].iloc[-5] * 100

        rs = stock_return - nifty_return

        if rs >= 3:

            score += 40

            reasons.append("🚀 Strong Relative Strength")

        elif rs >= 1:

            score += 20

            reasons.append("🟢 Better Than Nifty")

        elif rs <= -3:

            score -= 40

            reasons.append("🔴 Very Weak vs Nifty")

        elif rs <= -1:

            score -= 20

            reasons.append("⚠️ Underperforming Nifty")

    except Exception:

        pass

    return score, reasons
