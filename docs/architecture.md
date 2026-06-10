# Architecture

RefLens AI is a Streamlit-based prototype that explains football referee and VAR decisions using rule context, decision logic, and AI-generated explanation design.

## Current MVP Architecture

```text
User
 |
 v
Streamlit App
 |
 v
Decision Type + Match Moment Input
 |
 v
Rule-Based Decision Engine
 |
 v
Rule Retriever
 |
 v
Explanation Generator
 |
 v
Decision Explanation + Rule Applied + Confidence + Fan Disagreement
```

## Main Components

### Streamlit App

The Streamlit app provides the user interface. Fans can select a decision type, choose a demo scenario, describe a match moment, and select an explanation mode.

### Decision Engine

The decision engine uses simple rule-based logic to identify whether a decision is likely supported, uncertain, or needs review.

File: `src/decision_engine.py`

### Rule Retriever

The rule retriever provides relevant football rule context for the selected decision type.

File: `src/rule_retriever.py`

### Explanation Generator

The explanation generator turns the decision analysis and rule context into readable output for fans.

File: `src/explanation_generator.py`

### Granite Client

The Granite client file shows where IBM Granite integration will be connected in a future version.

File: `src/granite_client.py`

## Planned IBM AI Architecture

```text
User Input
 |
 v
Streamlit App
 |
 v
Rule Retriever
 |
 v
Langflow Workflow
 |
 v
IBM Granite Prompt
 |
 v
IBM Granite Explanation
 |
 v
Streamlit Output
```

## Future Improvements

- Connect live IBM Granite API.
- Build the workflow in Langflow.
- Use Docling to process official rule documents.
- Add multilingual explanations.
- Add more referee decision categories.
- Add richer confidence scoring.
