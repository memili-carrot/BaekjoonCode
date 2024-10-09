def max_sticker_score(t, test_cases):
    results = []
    for _ in range(t):
        n = test_cases[_][0]
        stickers = test_cases[_][1]
        
        if n == 1:
            results.append(max(stickers[0][0], stickers[1][0]))
            continue
        
        prev1_0 = stickers[0][0]
        prev1_1 = stickers[1][0]
        prev2_0 = 0
        prev2_1 = 0
        
        for i in range(1, n):
            current_0 = stickers[0][i] + max(prev1_1, prev2_1)
            current_1 = stickers[1][i] + max(prev1_0, prev2_0)
            prev2_0, prev2_1 = prev1_0, prev1_1
            prev1_0, prev1_1 = current_0, current_1      
        results.append(max(prev1_0, prev1_1))  
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))
    test_cases.append((n, stickers))

results = max_sticker_score(t, test_cases)
for result in results:
    print(result)