from collections import Counter
import math

def min_sets_for_room_number(room_number):
    count = Counter(room_number)
    six_nine_count = count.get('6', 0) + count.get('9', 0)
    count['6'] = count['9'] = math.ceil(six_nine_count / 2)
    
    return max(count.values())
room_number = input().strip()
print(min_sets_for_room_number(room_number))