import sys
input = sys.stdin.readline

def calculate():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        much = list(map(int, input().split()))
        per_person = m // n
        total = sum(min(money, per_person) for money in much)
        print(total)

if __name__ == '__main__':
    calculate()