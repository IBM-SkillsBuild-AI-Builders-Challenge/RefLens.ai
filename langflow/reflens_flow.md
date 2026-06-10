# RefLens AI Langflow Workflow

This file documents the planned Langflow workflow for RefLens AI.

## Goal

Use Langflow to organize the AI explanation pipeline for referee and VAR decisions.

## Workflow

```text
User Input
   |
   v
Decision Type + Match Moment
   |
   v
Rule Retriever
   |
   v
Relevant Football Rule Context
   |
   v
IBM Granite Prompt
   |
   v
Generated Explanation
   |
   v
Streamlit App Output
