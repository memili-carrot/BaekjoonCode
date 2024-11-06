import sys
input = sys.stdin.read

def round_half_up(value):
    return int(value + 0.5)

def calculate_mean(n, opinions):
    if n == 0:
        return 0

    opinions.sort()
    trim_count = round_half_up(n * 0.15)
    trimmed_sum = sum(opinions[trim_count:n - trim_count])
    trimmed_count = n - 2 * trim_count
    return round_half_up(trimmed_sum / trimmed_count)

data = input().splitlines()
n = int(data[0])
opinions = list(map(int, data[1:]))

print(calculate_mean(n, opinions))