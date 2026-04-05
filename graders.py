def grade_action(action, gold):
    score = 0.0
    details = []

    # ✅ Category check
    if action.category == gold["category"]:
        score += 0.3
        details.append("correct category")
    else:
        details.append("wrong category")

    # ✅ Priority check
    if action.priority == gold["priority"]:
        score += 0.2
        details.append("correct priority")
    else:
        details.append("wrong priority")

    # ✅ Decision check
    if action.decision == gold["decision"]:
        score += 0.4
        details.append("correct decision")
    else:
        details.append("wrong decision")

    # ✅ Reply quality (basic heuristic)
    if action.reply and len(action.reply) > 15:
        score += 0.1
        details.append("good reply")
    else:
        details.append("weak/no reply")

    # Clamp score between 0 and 1
    score = max(0.0, min(score, 1.0))

    return score, ", ".join(details)