import sys
input = sys.stdin.read

def max_sticker_score(t, test_cases):
    results = []
    for n, stickers in test_cases:
        if n == 1:
            results.append(max(stickers[0][0], stickers[1][0]))
            continue
        prev1_0, prev1_1 = stickers[0][0], stickers[1][0]
        prev2_0, prev2_1 = 0, 0
        
        for i in range(1, n):
            current_0 = stickers[0][i] + max(prev1_1, prev2_1)
            current_1 = stickers[1][i] + max(prev1_0, prev2_0)
            prev2_0, prev2_1 = prev1_0, prev1_1
            prev1_0, prev1_1 = current_0, current_1      
        results.append(max(prev1_0, prev1_1))
    return results

data = input().splitlines()
t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    stickers = [list(map(int, data[index + 1].split())), list(map(int, data[index + 2].split()))]
    test_cases.append((n, stickers))
    index += 3

results = max_sticker_score(t, test_cases)
sys.stdout.write("\n".join(map(str, results)) + "\n")