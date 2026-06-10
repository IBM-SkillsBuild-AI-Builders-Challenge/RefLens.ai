# RefLens AI

## Explainable AI for Football Referee and VAR Decisions

RefLens AI is an AI-powered football companion that helps fans understand controversial referee and VAR decisions. It explains the decision, the rule applied, the confidence level, and why fans may disagree.

Built for the IBM SkillsBuild AI Builders Challenge.

---

## Overview

Football fans often see controversial calls such as handballs, offsides, penalties, red cards, and fouls before goals without understanding the rule or reasoning behind the decision.

RefLens AI solves this problem by turning referee and VAR decisions into clear, educational explanations.

The app is built with Streamlit and designed around IBM AI technologies including IBM Granite, Langflow, and Docling.

---

## Problem

During football matches, controversial decisions can confuse fans and create frustration. Many fans do not know:

- What rule applies
- Why a decision was made
- What evidence matters
- Why another fan may disagree
- How uncertain the decision may be

This lack of explanation can reduce trust and make the game harder to understand.

---

## Solution

RefLens AI helps fans understand referee and VAR decisions by explaining:

- The decision summary
- The rule applied
- The confidence level
- Why fans may disagree
- The uncertainty behind the call

It is designed as an educational assistant, not a replacement for referees or VAR officials.

---

## Features

- Demo scenarios for common controversial decisions
- Custom match moment input
- Beginner, Expert, 10-second summary, and “Why fans are upset” explanation modes
- Rule-based decision analysis
- Rule context retrieval
- Confidence-level explanation
- Fan disagreement explanation
- Responsible AI note
- IBM Granite, Langflow, and Docling integration plan

---

## Supported Decision Types

The MVP supports:

- Handball
- Offside
- Penalty
- Red card
- Foul before goal

---

## IBM AI Integration

RefLens AI is designed around IBM AI technologies.

### IBM Granite

IBM Granite is the planned generative AI model for producing clear, responsible explanations of referee and VAR decisions.

In the current MVP, local Python logic generates explanations so the project can run without API credentials. The file `src/granite_client.py` shows where Granite integration will be connected.

### Langflow

Langflow is used to design the decision-explanation workflow:

```text
User input → Rule retrieval → Prompt construction → IBM Granite explanation → Streamlit output
```

The planned workflow is documented in `langflow/reflens_flow.md`.

### Docling

Docling will be used to process football rule documents into structured text. This allows RefLens AI to retrieve relevant rule context before generating an explanation.

The Docling integration plan is documented in `docs/docling_plan.md`.

---

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/reflens-ai.git
cd reflens-ai
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the local Streamlit URL in your browser.

---

## Repository Structure

```text
reflens-ai/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── decision_engine.py
│   ├── explanation_generator.py
│   ├── rule_retriever.py
│   ├── confidence_score.py
│   └── granite_client.py
│
├── docs/
│   ├── architecture.md
│   ├── challenge_alignment.md
│   ├── demo_script.md
│   ├── docling_plan.md
│   └── responsible_ai.md
│
└── langflow/
    └── reflens_flow.md
```

---

## Responsible AI

RefLens AI is designed as an educational assistant.

It does not:

- Replace official referees
- Replace VAR officials
- Make official match decisions
- Claim certainty when evidence is limited

The app explains uncertainty, provides confidence levels, and reminds users that real referee decisions may require video evidence, camera angles, timing, and official interpretation.

More details are available in `docs/responsible_ai.md`.

---

## Future Improvements

Future versions could include:

- Live IBM Granite API connection
- Full Langflow workflow export
- Docling-processed official rule documents
- Multilingual explanations
- More referee decision types
- Better confidence scoring
- Live match event data
- Audio narration for accessibility

---

## Project Status

Working MVP completed.

The current version runs locally as a Streamlit app and demonstrates the full RefLens AI explanation flow using local rule-based logic with a documented IBM AI integration plan.
