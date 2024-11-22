n = int(input())
problems = [input().split() for _ in range(n)]
problems = [(title, int(difficulty)) for title, difficulty in problems]
print(min(problems, key=lambda x: x[1])[0])