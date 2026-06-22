# ここから書きましょう
scores = [56, 82, 73, 91, 68, 45, 88]
def high_scores(scores):
    high_scores_list = []
    for score in scores:
        if score >= 80:
            high_scores_list.append(score)
    return high_scores_list
print(high_scores(scores))
print(len(high_scores(scores)))