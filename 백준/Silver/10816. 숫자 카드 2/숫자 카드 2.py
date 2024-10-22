from collections import Counter
N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

card_count = Counter(cards)

result = [card_count[target] for target in targets]
print(" ".join(map(str, result)))