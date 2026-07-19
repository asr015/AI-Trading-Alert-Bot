# ==========================================
# TradingASR AI Pro v3.1
# File : option_chain.py
# ==========================================

from nse_engine import get_option_chain


def analyze_option_chain():

    default_response = {
        "PCR": "N/A",
        "MaxPain": "N/A",
        "HighestCallOI": "N/A",
        "HighestPutOI": "N/A",
        "CallWriting": "N/A",
        "PutWriting": "N/A",
        "MarketBias": "UNKNOWN"
    }

    try:

        data = get_option_chain()

        # NSE unavailable
        if not data:
            return default_response

        records = data.get("records", {}).get("data", [])

        if not records:
            return default_response

        total_ce_oi = 0
        total_pe_oi = 0

        call_oi = {}
        put_oi = {}

        max_ce = 0
        max_pe = 0

        call_strike = "-"
        put_strike = "-"
        max_pain = "-"

        for row in records:

            strike = row.get("strikePrice")

            ce = row.get("CE")
            if ce:
                oi = ce.get("openInterest", 0)
                total_ce_oi += oi
                call_oi[strike] = oi

                if oi > max_ce:
                    max_ce = oi
                    call_strike = strike

            pe = row.get("PE")
            if pe:
                oi = pe.get("openInterest", 0)
                total_pe_oi += oi
                put_oi[strike] = oi

                if oi > max_pe:
                    max_pe = oi
                    put_strike = strike

        pcr = (
            round(total_pe_oi / total_ce_oi, 2)
            if total_ce_oi else "N/A"
        )

        common = set(call_oi) & set(put_oi)

        if common:
            max_pain = max(
                common,
                key=lambda x: call_oi[x] + put_oi[x]
            )

        if pcr == "N/A":
            bias = "UNKNOWN"
        elif pcr >= 1.20:
            bias = "BULLISH"
        elif pcr <= 0.80:
            bias = "BEARISH"
        else:
            bias = "SIDEWAYS"

        return {
            "PCR": pcr,
            "MaxPain": max_pain,
            "HighestCallOI": max_ce,
            "HighestPutOI": max_pe,
            "CallWriting": call_strike,
            "PutWriting": put_strike,
            "MarketBias": bias
        }

    except Exception as e:

        print(f"Option Chain Error : {e}")

        return default_response
