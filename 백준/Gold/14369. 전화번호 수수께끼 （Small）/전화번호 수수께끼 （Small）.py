def decode_number(s, case_num):
    unique_chars = {'Z': 0, 'G': 8, 'X': 6, 'W': 2, 'U': 4, 'F': 5, 'H': 3, 'I': 9, 'V': 7, 'O': 1}
    count = {unique_chars[k]: s.count(k) for k in unique_chars}

    count[3] -= count[8]
    count[5] -= count[4]
    count[7] -= count[5]
    count[9] -= count[5] + count[6] + count[8]
    count[1] -= count[0] + count[2] + count[4]

    result = ''.join(str(i) * count[i] for i in sorted(count))
    return f"Case #{case_num}: {result}"

t = int(input())
for i in range(1, t + 1):
    s = input().strip()
    print(decode_number(s, i))