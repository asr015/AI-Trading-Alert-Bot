def get_risk(score):

    if score >= 90:
        return "🟢 LOW"

    elif score >= 75:
        return "🟡 MEDIUM"

    else:
        return "🔴 HIGH"
