# RefLens AI

An Explainable AI Companion for Football Referee and VAR Decisions.

## Overview

RefLens AI helps football fans understand controversial referee and VAR decisions in plain language. It explains the rule involved, the match context, the reasoning behind the decision, the uncertainty level, and why fans may disagree.

## Problem

Football fans often see controversial decisions such as offside, handball, penalties, and red cards without clear explanations. This causes confusion, frustration, and mistrust.

## Solution

RefLens AI uses AI to explain referee and VAR decisions using rule-based context and IBM Granite-powered natural language explanations.

## IBM Technology Used

- IBM Granite for natural-language decision explanations
- Langflow for AI workflow orchestration
- Docling for processing football rule documents
- IBM SkillsBuild learning resources

## Features

- VAR decision explanation
- Rule-based reasoning
- Confidence score
- Beginner and expert explanation modes
- Fan disagreement explanation
- Responsible AI disclaimer

## Demo

The MVP is built with Streamlit.

## How to Run Locally

```bash
git clone https://github.com/YOUR-USERNAME/reflens-ai.git
cd reflens-ai
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py]
```
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
