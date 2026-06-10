import streamlit as st
from src.decision_engine import analyze_decision
from src.explanation_generator import generate_explanation

st.set_page_config(page_title="RefLens AI", page_icon="⚽")

st.title("RefLens AI")
st.subheader("Explainable AI for Football Referee and VAR Decisions")

st.write(
    "RefLens AI helps fans understand controversial decisions by explaining "
    "the rule, the reasoning, the uncertainty, and why fans may disagree."
)

decision_type = st.selectbox(
    "Decision type",
    ["Offside", "Handball", "Penalty", "Red Card", "Foul Before Goal"]
)

match_moment = st.text_area(
    "Describe the match moment",
    "A defender blocked a shot inside the penalty area with an arm extended away from the body."
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
