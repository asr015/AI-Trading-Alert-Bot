# ==========================================
# TradingASR AI Pro v4.0
# File : master_ai_engine.py
# Part 1 / 5
# ==========================================

from market_bias_engine import market_bias_score

# Future Ready
try:
    from news_engine import news_score
except ImportError:

    def news_score(symbol):
        return 0, []

# ==========================================
# OPTION CHAIN CACHE
# ==========================================

_option_cache = None


def set_option_chain(option_data):

    global _option_cache

    _option_cache = option_data


# ==========================================
# CONFIDENCE ENGINE
# ==========================================

def calculate_confidence(score, reasons):

    confidence = 50

    # Score contribution
    confidence += min(abs(score) // 10, 30)

    # Confirmation contribution
    confidence += min(len(reasons) * 2, 20)

    confidence = max(50, min(99, int(confidence)))

    return f"{confidence}%"
    # ==========================================
# SCORE NORMALIZATION
# ==========================================

def normalize_score(score):

    if score > 500:
        return 500

    elif score < -500:
        return -500

    return int(score)


# ==========================================
# AI VERDICT ENGINE
# ==========================================

def generate_verdict(score):

    if score >= 420:

        return {
            "verdict": "🔥 ELITE BUY",
            "signal": "BUY"
        }

    elif score >= 300:

        return {
            "verdict": "🚀 STRONG BUY",
            "signal": "BUY"
        }

    elif score >= 180:

        return {
            "verdict": "🟢 BUY",
            "signal": "BUY"
        }

    elif score <= -420:

        return {
            "verdict": "💥 ELITE SELL",
            "signal": "SELL"
        }

    elif score <= -300:

        return {
            "verdict": "🔴 STRONG SELL",
            "signal": "SELL"
        }

    elif score <= -180:

        return {
            "verdict": "🟥 SELL",
            "signal": "SELL"
        }

    else:

        return {
            "verdict": "🟡 WAIT",
            "signal": "WAIT"
        }


# ==========================================
# REMOVE DUPLICATE REASONS
# ==========================================

def clean_reasons(reasons):

    cleaned = []

    for reason in reasons:

        if reason not in cleaned:
            cleaned.append(reason)

    return cleaned[:12]
    # ==========================================
# FINAL AI ENGINE
# ==========================================

def final_ai_score(symbol, scanner_score):

    global _option_cache

    score = scanner_score

    reasons = []

    # ======================================
    # MARKET BIAS ENGINE
    # ======================================

    market = market_bias_score()

    if isinstance(market, dict):

        score += market.get("score", 0)

        reasons.extend(
            market.get("reasons", [])
        )

    # ======================================
    # OPTION CHAIN CONFIRMATION
    # ======================================

    if _option_cache:

        pcr = _option_cache.get("PCR", "N/A")

        bias = _option_cache.get(
            "MarketBias",
            "UNKNOWN"
        )

        if isinstance(pcr, (int, float)):

            if pcr >= 1.20:

                score += 25

                reasons.append(
                    f"🟢 Bullish PCR ({pcr:.2f})"
                )

            elif pcr <= 0.80:

                score -= 25

                reasons.append(
                    f"🔴 Bearish PCR ({pcr:.2f})"
                )

        if bias == "BULLISH":

            score += 15

            reasons.append(
                "📈 Option Chain Bullish"
            )

        elif bias == "BEARISH":

            score -= 15

            reasons.append(
                "📉 Option Chain Bearish"
            )

    # ======================================
    # NEWS ENGINE (Future Ready)
    # ======================================

    news_points, news_reasons = news_score(symbol)

    score += news_points

    reasons.extend(news_reasons)

    # ======================================
    # SCORE NORMALIZATION
    # ======================================

    score = normalize_score(score)
        # ======================================
    # CONFIDENCE ENGINE
    # ======================================

    reasons = clean_reasons(reasons)

    confidence = calculate_confidence(
        score,
        reasons
    )

    # ======================================
    # AI VERDICT
    # ======================================

    decision = generate_verdict(score)

    verdict = decision["verdict"]

    signal = decision["signal"]

    # ======================================
    # RISK FILTER
    # ======================================

    if signal == "BUY":

        bearish = sum(
            1 for r in reasons
            if any(
                x in r.lower()
                for x in [
                    "bearish",
                    "selling",
                    "breakdown",
                    "lower",
                    "supply"
                ]
            )
        )

        if bearish >= 4:

            verdict = "🟡 WAIT"

            signal = "WAIT"

            reasons.append(
                "⚠️ Bullish setup rejected by AI Risk Filter"
            )

    elif signal == "SELL":

        bullish = sum(
            1 for r in reasons
            if any(
                x in r.lower()
                for x in [
                    "bullish",
                    "buying",
                    "breakout",
                    "higher",
                    "demand"
                ]
            )
        )

        if bullish >= 4:

            verdict = "🟡 WAIT"

            signal = "WAIT"

            reasons.append(
                "⚠️ Bearish setup rejected by AI Risk Filter"
            )

    reasons = clean_reasons(reasons)
