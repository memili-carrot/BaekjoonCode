import sys
from decimal import Decimal, ROUND_HALF_UP

input = sys.stdin.readline

T = int(input())

dic = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0.0
}

time_all = []
score_all = []

for _ in range(T):
    subject, time, grade = input().split()
    time_all.append(int(time))
    score_all.append(dic[grade])
weighted_gpa_sum = sum(a * b for a, b in zip(time_all, score_all))
total_credits = sum(time_all)
gpa = Decimal(weighted_gpa_sum) / Decimal(total_credits)
rounded_gpa = gpa.quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)

print(f"{rounded_gpa:.2f}")