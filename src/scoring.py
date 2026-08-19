def calculate_score(indicators):
    score = 100 - (len(indicators) * 10)

    if score < 0:
        score = 0

    return score