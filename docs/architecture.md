# Architecture

User input goes into the Streamlit app.

The app sends the decision type and match moment to the rule-based decision engine.

The rule retriever provides relevant football rule context.

The explanation generator creates a fan-friendly explanation.

Future version:
The explanation generator will call IBM Granite through Langflow to produce grounded natural-language responses.
