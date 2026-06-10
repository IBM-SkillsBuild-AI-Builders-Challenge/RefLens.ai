from src.rule_retriever import get_rule_context
from src.confidence_score import format_confidence

def generate_explanation(decision_type, match_moment, explanation_mode, analysis):
    rule = get_rule_context(decision_type)
    confidence = format_confidence(analysis["confidence"], analysis["reason"])

    if explanation_mode == "10-second summary":
        summary = (
            f"{analysis['likely_decision']}. "
            f"{analysis['reason']}"
        )
    elif explanation_mode == "Why fans are upset":
        summary = (
            f"Fans may be upset because {decision_type.lower()} decisions often depend on small details "
            f"that are hard to see in real time."
        )
    elif explanation_mode == "Expert":
        summary = (
            f"The decision type is {decision_type}. Based on the provided match context, "
            f"the system assessment is: {analysis['likely_decision']}. "
            f"The key reasoning factor is: {analysis['reason']}"
        )
    else:
        summary = (
            f"This decision is about {decision_type.lower()}. "
            f"Based on the match description, RefLens AI says: {analysis['likely_decision']}. "
            f"The main reason is: {analysis['reason']}"
        )

    fan_disagreement = (
        "Fans may disagree because referee decisions depend on camera angle, timing, intent, "
        "player movement, and how clearly the evidence supports the call."
    )

    return {
        "summary": summary,
        "rule": rule,
        "confidence": confidence,
        "fan_disagreement": fan_disagreement
    }
