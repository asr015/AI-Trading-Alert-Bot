# ==========================================
# TradingASR AI Pro v3.0
# File : trend_strength_engine.py
# ==========================================

import pandas as pd


def trend_strength_score(df):

    score = 0
    reasons = []

    if len(df) < 20:
        return score, reasons

    high = df["High"]
    low = df["Low"]
    close = df["Close"]

    plus_dm = high.diff()
    minus_dm = -low.diff()

    plus_dm = plus_dm.where(
        (plus_dm > minus_dm) & (plus_dm > 0),
        0
    )

    minus_dm = minus_dm.where(
        (minus_dm > plus_dm) & (minus_dm > 0),
        0
    )

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    tr = pd.concat(
        [tr1, tr2, tr3],
        axis=1
    ).max(axis=1)

    atr = tr.rolling(14).mean()

    plus_di = (
        100 *
        (plus_dm.rolling(14).mean() / atr)
    )

    minus_di = (
        100 *
        (minus_dm.rolling(14).mean() / atr)
    )

    dx = (
        (plus_di - minus_di).abs()
        /
        (plus_di + minus_di)
    ) * 100

    adx = dx.rolling(14).mean()

    last_adx = adx.iloc[-1]
    last_plus = plus_di.iloc[-1]
    last_minus = minus_di.iloc[-1]

    if last_adx > 25:

        score += 30
        reasons.append("✅ Strong Trend (ADX)")

    elif last_adx < 18:

        score -= 20
        reasons.append("⚠️ Sideways Market")

    if last_plus > last_minus:

        score += 20
        reasons.append("🟢 Buyers Dominating")

    else:

        score -= 20
        reasons.append("🔴 Sellers Dominating")

    return score, reasons
