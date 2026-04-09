def grader_easy(state, action):
    return 0.8 if action.get("value") == "spam" else 0.3


def grader_medium(state, action):
    return 0.7 if action.get("value") == "spam" else 0.4


def grader_hard(state, action):
    return 0.75 if action.get("value") == "not_spam" else 0.2
