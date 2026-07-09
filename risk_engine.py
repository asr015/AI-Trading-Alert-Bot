def calculate_trade(df, score):

    last = df.iloc[-1]

    atr = last["ATR"]

    # BUY
    if score >= 0:

        entry = round(last["High"] + atr * 0.20, 2)

        sl = round(last["Low"] - atr * 0.50, 2)

        risk = entry - sl

        target1 = round(entry + risk * 2, 2)

        target2 = round(entry + risk * 3, 2)

        trade = "BUY"

    # SELL
    else:

        entry = round(last["Low"] - atr * 0.20, 2)

        sl = round(last["High"] + atr * 0.50, 2)

        risk = sl - entry

        target1 = round(entry - risk * 2, 2)

        target2 = round(entry - risk * 3, 2)

        trade = "SELL"

    return {
        "trade": trade,
        "entry": entry,
        "sl": sl,
        "target1": target1,
        "target2": target2
    }
