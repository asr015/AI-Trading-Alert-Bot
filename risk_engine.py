# ==========================================
# TradingASR AI Pro v2.2
# File : risk_engine.py
# ==========================================

def calculate_trade(df, score):

    last = df.iloc[-1]

    atr = last.get("ATR", 0)

    # ATR missing ya invalid ho
    if atr <= 0:
        atr = (last["High"] - last["Low"]) * 0.50

    # BUY
    if score >= 0:

        entry = round(last["High"] + atr * 0.20, 2)
        sl = round(last["Low"] - atr * 0.50, 2)

        risk = max(entry - sl, 0.01)

        target1 = round(entry + risk * 2, 2)
        target2 = round(entry + risk * 3, 2)

        trade = "BUY"

    # SELL
    else:

        entry = round(last["Low"] - atr * 0.20, 2)
        sl = round(last["High"] + atr * 0.50, 2)

        risk = max(sl - entry, 0.01)

        target1 = round(entry - risk * 2, 2)
        target2 = round(entry - risk * 3, 2)

        trade = "SELL"

    rr = round(abs(target1 - entry) / risk, 2)

    return {
        "trade": trade,
        "entry": entry,
        "sl": sl,
        "target1": target1,
        "target2": target2,
        "risk_reward": rr
    }
