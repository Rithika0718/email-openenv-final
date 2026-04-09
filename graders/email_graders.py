def grader_easy(state, action):
    if action.get("value") == "spam":
        return 0.8
    return 0.3


def grader_medium(state, action):
    if action.get("value") == "spam":
        return 0.7
    return 0.4


def grader_hard(state, action):
    if action.get("value") == "not_spam":
        return 0.75
    return 0.2
