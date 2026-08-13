def calculate_mac(pattern, filter_data):
    score = 0.0

    for r in range(len(pattern)):
        for c in range(len(pattern[r])):
            score += pattern[r][c] * filter_data[r][c]

    return score
