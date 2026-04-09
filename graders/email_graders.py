def clamp_score(value):
    # ensures score NEVER becomes 0.0 or 1.0
    if value <= 0.0:
        return 0.1
    if value >= 1.0:
        return 0.9
    return value


def grader_easy(state, action):
    score = 0.8 if action.get("value") == "spam" else 0.3
    return clamp_score(score)


def grader_medium(state, action):
    score = 0.7 if action.get("value") == "spam" else 0.4
    return clamp_score(score)


def grader_hard(state, action):
    score = 0.75 if action.get("value") == "not_spam" else 0.2
    return clamp_score(score)
