def analyze_decision(decision_type, match_moment):
    text = match_moment.lower()

    if decision_type == "Handball":
        if "extended" in text or "away from the body" in text or "unnatural" in text:
            return {
                "likely_decision": "Penalty likely supported",
                "reason": "The arm appears to make the body unnaturally bigger.",
                "confidence": "Medium"
            }
        return {
            "likely_decision": "Decision uncertain",
            "reason": "The description does not provide enough detail about arm position or reaction time.",
            "confidence": "Low"
        }

    if decision_type == "Offside":
        if "ahead" in text or "second-last defender" in text:
            return {
                "likely_decision": "Offside likely supported",
                "reason": "The attacker appears to be ahead of the second-last defender when the ball was played.",
                "confidence": "Medium"
            }
        return {
            "likely_decision": "Decision uncertain",
            "reason": "Offside requires the attacker position at the exact moment the pass is played.",
            "confidence": "Low"
        }

    if decision_type == "Red Card":
        if "serious foul" in text or "violent" in text or "studs" in text:
            return {
                "likely_decision": "Red card likely supported",
                "reason": "The action may involve serious foul play or violent conduct.",
                "confidence": "Medium"
            }
        return {
            "likely_decision": "Decision uncertain",
            "reason": "More detail is needed about force, contact point, and player safety risk.",
            "confidence": "Low"
        }

    return {
        "likely_decision": "Decision needs review",
        "reason": "The available context is limited.",
        "confidence": "Low"
    }
