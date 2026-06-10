from src.rule_retriever import get_rule_context
from src.confidence_score import format_confidence


def generate_explanation(decision_type, match_moment, explanation_mode, analysis):
    rule = get_rule_context(decision_type)
    confidence = format_confidence(analysis["confidence"], analysis["reason"])

    if explanation_mode == "10-second summary":
        summary = (
            f"{analysis['likely_decision']}. "
            f"Main reason: {analysis['reason']}"
        )

    elif explanation_mode == "Why fans are upset":
        summary = (
            f"Fans may be upset because this {decision_type.lower()} decision depends on small details "
            f"that are hard to judge in real time. The system assessment is: "
            f"{analysis['likely_decision']}. The key issue is: {analysis['reason']}"
        )

    elif explanation_mode == "Expert":
        summary = (
            f"The reviewed incident is categorized as {decision_type}. "
            f"Based on the provided match context, RefLens AI assesses the decision as: "
            f"{analysis['likely_decision']}. The primary decision factor is: "
            f"{analysis['reason']} This type of call may require precise timing, positioning, "
            f"camera angle review, and referee interpretation."
        )

    else:
        summary = (
            f"This decision is about {decision_type.lower()}. "
            f"In simple terms, RefLens AI says: {analysis['likely_decision']}. "
            f"The main reason is: {analysis['reason']}"
        )

    if explanation_mode == "10-second summary":
        fan_disagreement = (
            "Fans may disagree because the call can look different depending on the camera angle."
        )
    elif explanation_mode == "Why fans are upset":
        fan_disagreement = (
            "Fans may disagree because emotional moments, slow-motion replays, team loyalty, "
            "camera angles, and unclear evidence can make the same decision feel unfair to different people."
        )
    elif explanation_mode == "Expert":
        fan_disagreement = (
            "Disagreement may come from interpretation of intent, timing, point of contact, "
            "player movement, match context, and whether the evidence meets the standard for review."
        )
    else:
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
