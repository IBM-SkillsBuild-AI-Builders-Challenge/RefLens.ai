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
```

## Inputs

- Decision type
- Match moment description
- Explanation mode
- Rule context
- Confidence score

## Output

The workflow returns:

- Decision explanation
- Rule applied
- Confidence level
- Uncertainty statement
- Why fans may disagree

## Current MVP Status

The current app uses local Python logic to simulate the decision explanation process.

The Langflow workflow is documented here and can later be implemented by connecting the rule retriever, prompt template, and IBM Granite model node.
