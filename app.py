import streamlit as st
from src.decision_engine import analyze_decision
from src.explanation_generator import generate_explanation


st.set_page_config(page_title="RefLens AI", page_icon="⚽", layout="centered")


# Sidebar
st.sidebar.title("RefLens AI")
st.sidebar.write("IBM SkillsBuild AI Builders Challenge")

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    **Purpose:**  
    Help fans understand referee and VAR decisions.

    **Built with:**  
    - Streamlit  
    - IBM Granite plan  
    - Langflow workflow plan  
    - Docling rule-processing plan
    """
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Educational prototype only. Does not replace official referee or VAR decisions."
)


# Main header
st.title("RefLens AI")
st.subheader("Explainable AI for Football Referee and VAR Decisions")

st.write(
    "RefLens AI helps football fans understand controversial calls by explaining "
    "the rule, the reasoning, the uncertainty, and why fans may disagree."
)

st.info(
    "Select a demo scenario or describe your own match moment to generate an explanation."
)


# IBM section
with st.expander("IBM AI Technology Used"):
    st.markdown(
        """
        **RefLens AI is designed for the IBM SkillsBuild AI Builders Challenge.**

        This prototype uses an IBM-focused AI architecture:

        - **IBM Granite**: Planned model for natural-language referee and VAR explanations.
        - **Langflow**: Planned workflow from user input to rule retrieval to AI explanation.
        - **Docling**: Planned tool for processing football rule documents into structured text.
        - **Responsible AI**: The app explains uncertainty and avoids replacing human officials.

        **Current MVP note:** This version uses local Python logic so it can run without API keys.
        The Granite/Langflow/Docling layer is documented and prepared for integration.
        """
    )


# Demo scenarios
examples = {
    "Custom": (
        "Handball",
        "A defender blocked a shot inside the penalty area with an arm extended away from the body."
    ),
    "Handball: arm extended in box": (
        "Handball",
        "A defender blocked a shot inside the penalty area with an arm extended away from the body."
    ),
    "Offside: attacker ahead of second-last defender": (
        "Offside",
        "The attacker was ahead of the second-last defender when the pass was played and then scored."
    ),
    "Red card: studs-up tackle": (
        "Red Card",
        "A player made a studs-up tackle with high force near the opponent's ankle."
    ),
    "Penalty: late tackle inside box": (
        "Penalty",
        "A defender made late contact with an attacker inside the penalty area after missing the ball."
    ),
    "Foul before goal: attacking push": (
        "Foul Before Goal",
        "An attacker pushed a defender before the goal was scored."
    )
}

scenario = st.selectbox(
    "Try a demo scenario",
    list(examples.keys())
)

default_decision_type, default_moment = examples[scenario]

decision_options = ["Offside", "Handball", "Penalty", "Red Card", "Foul Before Goal"]

decision_type = st.selectbox(
    "Decision type",
    decision_options,
    index=decision_options.index(default_decision_type)
)

match_moment = st.text_area(
    "Describe the match moment",
    default_moment
)

explanation_mode = st.selectbox(
    "Explanation mode",
    ["Beginner", "Expert", "10-second summary", "Why fans are upset"]
)


# Generate explanation
if st.button("Explain Decision"):
    analysis = analyze_decision(decision_type, match_moment)
    explanation = generate_explanation(
        decision_type,
        match_moment,
        explanation_mode,
        analysis
    )

    st.success("Decision explanation generated.")

    st.header("RefLens Decision Summary")
    st.write(explanation["summary"])

    st.header("Rule Applied")
    st.write(explanation["rule"])

    st.header("Confidence Level")
    st.info(explanation["confidence"])

    st.header("Why Fans May Disagree")
    st.write(explanation["fan_disagreement"])

    with st.expander("Responsible AI Note"):
        st.write(
            "RefLens AI is an educational assistant. It does not replace official referees, "
            "VAR officials, or competition authorities. Real decisions may require video evidence, "
            "camera angles, timing, and official interpretation."
        )
