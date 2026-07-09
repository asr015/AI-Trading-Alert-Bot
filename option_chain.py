from nse_engine import get_option_chain


def analyze_option_chain():

    data = get_option_chain()

    records = data["records"]["data"]

    total_ce_oi = 0
    total_pe_oi = 0

    max_ce = 0
    max_pe = 0

    call_strike = None
    put_strike = None

    for row in records:

        if "CE" in row:

            ce = row["CE"]

            total_ce_oi += ce["openInterest"]

            if ce["openInterest"] > max_ce:

                max_ce = ce["openInterest"]

                call_strike = row["strikePrice"]


        if "PE" in row:

            pe = row["PE"]

            total_pe_oi += pe["openInterest"]

            if pe["openInterest"] > max_pe:

                max_pe = pe["openInterest"]

                put_strike = row["strikePrice"]


    if total_ce_oi == 0:

        pcr = 0

    else:

        pcr = round(total_pe_oi / total_ce_oi, 2)


    return {

        "PCR": pcr,

        "CallWriting": call_strike,

        "PutWriting": put_strike

    }
