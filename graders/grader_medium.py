def grade_medium(predicted_label, predicted_priority, correct_label, correct_priority):
    score = 0.0

    if predicted_label == correct_label:
        score += 0.5

    if predicted_priority == correct_priority:
        score += 0.5

    return score