def calculate_risk(score):

    if score >= 220:

        return {
            "risk": "🟢 LOW",
            "rr": "1:3"
        }

    elif score >= 160:

        return {
            "risk": "🟡 MEDIUM",
            "rr": "1:2"
        }

    else:

        return {
            "risk": "🔴 HIGH",
            "rr": "Avoid Trade"
        }
