def find_pairs_count(arr, x):
    num_set = set()
    count = 0
    
    for num in arr:
        if x - num in num_set:
            count += 1
        num_set.add(num)
    
    return count

n = int(input()) 
arr = list(map(int, input().split()))
x = int(input()) 

result = find_pairs_count(arr, x)
print(result)