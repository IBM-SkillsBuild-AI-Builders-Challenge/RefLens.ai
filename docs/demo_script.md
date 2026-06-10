# RefLens AI Demo Script

## 0:00–0:20 — Introduction

Hi, my project is RefLens AI, an explainable AI companion for football referee and VAR decisions.

It was built for the IBM SkillsBuild AI Builders Challenge.

## 0:20–0:45 — Problem

Football fans often see controversial decisions like handballs, offsides, penalties, red cards, or fouls before goals without understanding the rule or reasoning behind the call.

This can lead to confusion, frustration, and mistrust, especially during major tournaments.

## 0:45–1:15 — Solution

RefLens AI helps fans understand these decisions by explaining four things:

1. The decision summary
2. The rule that applies
3. The confidence level
4. Why fans may disagree

It is designed as an educational assistant, not a replacement for official referees or VAR officials.

## 1:15–2:00 — App Walkthrough

In the app, I can choose a demo scenario or describe my own match moment.

For example, I will choose the handball scenario where a defender blocks a shot inside the penalty area with an arm extended away from the body.

Then I select an explanation mode.

The app supports Beginner, Expert, 10-second summary, and Why fans are upset.

When I click Explain Decision, RefLens AI generates a decision summary, the rule applied, a confidence level, and an explanation of why fans may disagree.

## 2:00–2:30 — IBM Technology

RefLens AI is designed around IBM AI technologies.

IBM Granite is planned for generating natural-language decision explanations.

Langflow is planned for organizing the workflow from user input to rule retrieval to final explanation.

Docling is planned for processing football rule documents into structured text for retrieval.

The current MVP uses local Python logic so it can run without API keys, while the IBM integration layer is documented and prepared in the repository.

## 2:30–3:00 — Closing

RefLens AI makes football decisions easier to understand, more transparent, and more accessible for fans.

It supports responsible AI by explaining uncertainty, showing confidence levels, and making clear that official decisions remain with referees and VAR officials.
