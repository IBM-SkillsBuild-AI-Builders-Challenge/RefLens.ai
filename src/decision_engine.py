def analyze_decision(decision_type, match_moment):
    text = match_moment.lower()

    if decision_type == "Handball":
        if "extended" in text or "away from the body" in text or "unnatural" in text:
            return {
                "likely_decision": "Penalty likely supported",
                "reason": "The arm appears to make the body unnaturally bigger.",
                "confidence": "Medium"
            }

    if decision_type == "Offside":
        if "ahead" in text or "second-last defender" in text or "scored" in text:
            return {
                "likely_decision": "Offside likely supported",
                "reason": "The attacker appears to be in an offside position and involved in active play.",
                "confidence": "Medium"
            }

    if decision_type == "Red Card":
        if "studs" in text or "high force" in text or "violent" in text:
            return {
                "likely_decision": "Red card likely supported",
                "reason": "The challenge may endanger the safety of the opponent.",
                "confidence": "Medium"
            }

    if decision_type == "Penalty":
        if "inside the penalty area" in text or "inside box" in text or "inside the box" in text:
            return {
                "likely_decision": "Penalty likely supported",
                "reason": "The foul appears to happen inside the defending team's penalty area.",
                "confidence": "Medium"
            }

    if decision_type == "Foul Before Goal":
        if "pushed" in text or "push" in text or "foul" in text:
            return {
                "likely_decision": "Goal review likely supported",
                "reason": "An attacking foul may have occurred before the goal was scored.",
                "confidence": "Medium"
            }

    return {
        "likely_decision": "Decision uncertain",
        "reason": "The available description does not provide enough detail for a strong conclusion.",
        "confidence": "Low"
    }
