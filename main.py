# AI Emergency Response Assistant

def analyze_emergency(report):
    report = report.lower()

    score = 0

    critical_keywords = [
        "unconscious",
        "not breathing",
        "heart attack",
        "fire",
        "explosion"
    ]

    high_keywords = [
        "accident",
        "injured",
        "bleeding",
        "collapsed",
        "emergency"
    ]

    for word in critical_keywords:
        if word in report:
            score += 5

    for word in high_keywords:
        if word in report:
            score += 3

    # Determine priority
    if score >= 8:
        priority = "HIGH"
    elif score >= 3:
        priority = "MEDIUM"
    else:
        priority = "LOW"

    # Suggest response team
    if "fire" in report or "explosion" in report:
        team = "Fire Department"
    elif any(word in report for word in ["heart attack", "unconscious", "injured"]):
        team = "Ambulance"
    elif "crime" in report or "robbery" in report:
        team = "Police"
    else:
        team = "General Emergency Services"

    return priority, team


report = input("Describe the emergency: ")

priority, team = analyze_emergency(report)

print("\n--- Emergency Analysis ---")
print("Priority Level:", priority)
print("Dispatch:", team)
