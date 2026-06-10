RULES = {
    "Handball": (
        "Handball decisions consider whether the arm or hand made the body unnaturally bigger, "
        "whether the player had time to react, and whether the contact directly affected play."
    ),
    "Offside": (
        "A player may be offside if they are nearer to the opponent’s goal line than both the ball "
        "and the second-last opponent when the ball is played, and they become involved in active play."
    ),
    "Penalty": (
        "A penalty may be awarded when a defending player commits a direct free kick offense inside "
        "their own penalty area."
    ),
    "Red Card": (
        "A red card may be given for serious foul play, violent conduct, denying an obvious goal-scoring "
        "opportunity, or other sending-off offenses."
    ),
    "Foul Before Goal": (
        "A goal may be reviewed if an attacking foul happens in the attacking phase before the goal."
    )
}

def get_rule_context(decision_type):
    return RULES.get(decision_type, "No rule context found for this decision type.")
