def analyze_setup(score, reasons):

    confidence = 0
    verdict = "NO TRADE"

    # Score based confidence
    if score >= 200:
        confidence = 90

    elif score >= 150:
        confidence = 75

    elif score >= 100:
        confidence = 60

    else:
        confidence = 40


    # Smart Money check
    smart_money = False

    for r in reasons:

        if "Smart" in r or "Institutional" in r or "Breakout" in r:
            smart_money = True


    # Final Decision

    if score >= 150 and smart_money:

        verdict = "🔥 MOMENTUM BEFORE MOMENTUM"

    elif score >= 100:

        verdict = "🟢 WATCHLIST"

    else:

        verdict = "🔴 NO TRADE"


    return {

        "verdict": verdict,

        "confidence": f"{confidence}%"

  }
