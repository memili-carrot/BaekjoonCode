from itertools import combinations

s_list = list()
for _ in range(9):
    s_list.append(int(input()))

final_list = list()
for item in list(combinations(s_list,7)):
    if sum(list(item)) == 100:
        final_list = list(item)
        break
        
final_list.sort()
for i in final_list:
    print(i)