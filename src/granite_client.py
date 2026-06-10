"""
IBM Granite integration placeholder for RefLens AI.

The current MVP uses local Python logic so the app can run without API keys.
This file shows where IBM Granite will be connected later.
"""

import os
import requests


def generate_with_granite(decision_type, match_moment, rule_context, analysis):
    api_key = os.getenv("IBM_API_KEY")
    granite_url = os.getenv("IBM_GRANITE_URL")

    if not api_key or not granite_url:
        return None

    prompt = f"""
You are RefLens AI, an educational football referee decision assistant.

Explain this decision clearly and responsibly.

Decision type: {decision_type}
Match moment: {match_moment}
Rule context: {rule_context}
Analysis: {analysis}

Include:
1. Rule applied
2. Why the decision may be supported
3. What uncertainty exists
4. Why fans may disagree
5. Confidence level
"""

    payload = {"input": prompt}

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(granite_url, json=payload, headers=headers, timeout=20)
        response.raise_for_status()
        data = response.json()
        return data.get("generated_text") or data.get("output")
    except requests.RequestException:
        return None
