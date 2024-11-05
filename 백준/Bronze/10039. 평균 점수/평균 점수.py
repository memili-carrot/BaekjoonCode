scores = [int(input().strip()) for _ in range(5)]
total_score = sum(score if score >= 40 else 40 for score in scores)
average_score = total_score // 5

print(average_score)