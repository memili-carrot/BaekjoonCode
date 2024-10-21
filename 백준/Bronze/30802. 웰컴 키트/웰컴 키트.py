import sys
import math

N = int(sys.stdin.readline())
S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().split())
T, P = map(int, sys.stdin.readline().split())

total_tshirt_bundles = math.ceil(S / T) + math.ceil(M / T) + math.ceil(L / T) + \
                       math.ceil(XL / T) + math.ceil(XXL / T) + math.ceil(XXXL / T)

pen_bundles = N // P
remaining_pens = N % P

sys.stdout.write(f"{total_tshirt_bundles}\n")
sys.stdout.write(f"{pen_bundles} {remaining_pens}\n")