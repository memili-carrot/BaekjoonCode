def find_end_number(n):
    count = 0
    num = 666
    while True:
        if '666' in str(num):
            count += 1
            if count == n:
                return num
        num += 1

n = int(input())
print(find_end_number(n))