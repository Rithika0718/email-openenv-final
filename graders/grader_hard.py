def grade_hard(predicted_label, predicted_priority, reply_text, correct_label, correct_priority):
    score = 0.0

    if predicted_label == correct_label:
        score += 0.3

    if predicted_priority == correct_priority:
        score += 0.3

    if "sorry" in reply_text.lower():
        score += 0.4

    return score