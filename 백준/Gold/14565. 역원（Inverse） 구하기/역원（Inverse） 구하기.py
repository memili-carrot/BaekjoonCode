def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y
def inv(N, A):
    add_inv = (N - A) % N
    g, mul_inv, _ = egcd(A, N)
    if g != 1:
        mul_inv = -1
    else:
        mul_inv = mul_inv % N
    return add_inv, mul_inv
N, A = map(int, input().split())
add_inv, mul_inv = inv(N, A)
print(add_inv, mul_inv)