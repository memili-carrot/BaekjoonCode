K = int(input())

for class_num in range(1, K + 1):
    score = list(map(int, input().split()))
    N = score[0]
    score = score[1:]

    max_score = max(score)
    min_score = min(score)

    score.sort(reverse=True)
    largest_gap = max(score[i] - score[i + 1] for i in range(len(score) - 1))

    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")