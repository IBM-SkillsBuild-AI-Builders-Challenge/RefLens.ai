import streamlit as st
from src.decision_engine import analyze_decision
from src.explanation_generator import generate_explanation

st.set_page_config(page_title="RefLens AI", page_icon="⚽")

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

st.title("RefLens AI")
st.subheader("Explainable AI for Football Referee and VAR Decisions")

st.write(
    "RefLens AI helps fans understand controversial decisions by explaining "
    "the rule, the reasoning, the uncertainty, and why fans may disagree."
)

with st.expander("IBM AI Technology Used"):
    st.markdown(
        """
        **RefLens AI is designed for the IBM SkillsBuild AI Builders Challenge.**

        This prototype uses an IBM-focused AI architecture:

        - **IBM Granite**: Generates clear referee and VAR decision explanations.
        - **Langflow**: Organizes the workflow from user input to rule retrieval to AI explanation.
        - **Docling**: Processes football rule documents into structured text for retrieval.
        - **IBM SkillsBuild**: Supports learning, development, and responsible AI practices.

        Current MVP note: The app currently uses local rule-based logic as a working prototype.
        The Granite/Langflow/Docling layer is documented and prepared for integration.
        """
    )

decision_type = st.selectbox(
    "Decision type",
    ["Offside", "Handball", "Penalty", "Red Card", "Foul Before Goal"]
)
scenario = st.selectbox(
    "Try a demo scenario",
    [
        "Custom",
        "Handball: arm extended in box",
        "Offside: attacker ahead of second-last defender",
        "Red card: studs-up tackle",
        "Penalty: late tackle inside box",
        "Foul before goal: attacking push"
    ]
)

examples = {
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

if scenario != "Custom":
    decision_type = examples[scenario][0]
    default_moment = examples[scenario][1]
else:
    default_moment = "A defender blocked a shot inside the penalty area with an arm extended away from the body."
    
match_moment = st.text_area(
    "Describe the match moment",
    default_moment
)

explanation_mode = st.selectbox(
    "Explanation mode",
    ["Beginner", "Expert", "10-second summary", "Why fans are upset"]
)

if st.button("Explain Decision"):
    analysis = analyze_decision(decision_type, match_moment)
    explanation = generate_explanation(decision_type, match_moment, explanation_mode, analysis)

    st.header("Decision Explanation")
    st.write(explanation["summary"])

    st.header("Rule Applied")
    st.write(explanation["rule"])

    st.header("Confidence")
    st.info(explanation["confidence"])

    st.header("Why Fans May Disagree")
    st.write(explanation["fan_disagreement"])

    st.caption(
        "Responsible AI note: RefLens AI does not replace official referees or VAR officials. "
        "It provides educational explanations based on available context."
    )
