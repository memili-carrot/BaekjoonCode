visiting = list(map(int, input().split()))
home = list(map(int, input().split()))

def score(scores):
    T, F, S, P, C = scores
    return T * 6 + F * 3 + S * 2 + P * 1 + C * 2
visiting_score = score(visiting)
home_score = score(home)

print(visiting_score, home_score)