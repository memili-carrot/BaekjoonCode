def z_order(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    quadrant_size = half * half

    if r < half and c < half:
        return z_order(n - 1, r, c)
    elif r < half and c >= half:
        return quadrant_size + z_order(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * quadrant_size + z_order(n - 1, r - half, c)
    else:
        return 3 * quadrant_size + z_order(n - 1, r - half, c - half)

if __name__ == "__main__":
    n, r, c = map(int, input().split())
    print(z_order(n, r, c))