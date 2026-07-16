# ==========================================
# TradingASR AI Pro v3.0
# File : option_chain.py
# ==========================================

from nse_engine import get_option_chain


def analyze_option_chain():

    try:

        data = get_option_chain()

        records = data["records"]["data"]

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

            if "CE" in row:

                ce = row["CE"]

                oi = ce.get("openInterest", 0)

                total_ce_oi += oi

                call_oi[strike] = oi

                if oi > max_ce:

                    max_ce = oi

                    call_strike = strike

            if "PE" in row:

                pe = row["PE"]

                oi = pe.get("openInterest", 0)

                total_pe_oi += oi

                put_oi[strike] = oi

                if oi > max_pe:

                    max_pe = oi

                    put_strike = strike

        if total_ce_oi == 0:

            pcr = "N/A"

        else:

            pcr = round(total_pe_oi / total_ce_oi, 2)

        # ==========================
        # Max Pain
        # ==========================

        common = set(call_oi.keys()) & set(put_oi.keys())

        if common:

            max_pain = max(
                common,
                key=lambda x: call_oi[x] + put_oi[x]
            )

        # ==========================
        # Market Bias
        # ==========================

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

        print(e)

        return {

            "PCR": "N/A",

            "MaxPain": "N/A",

            "HighestCallOI": "N/A",

            "HighestPutOI": "N/A",

            "CallWriting": "N/A",

            "PutWriting": "N/A",

            "MarketBias": "UNKNOWN"

                }
