import sys
input = sys.stdin.readline

def is_inside(x, y, cx, cy, r):
    return(x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

def count(x1, y1, x2, y2, planets):
    count = 0
    for cx, cy, r in planets:
        inside_start = is_inside(x1, y1, cx, cy, r)
        inside_end = is_inside(x2, y2, cx, cy, r)
        if inside_start != inside_end:
            count += 1
    return count

def main():
    t = int(input())
    result = []
    for _ in range(t):
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        planets = [tuple(map(int, input().split())) for _ in range(n)]
        result.append(count(x1, y1, x2, y2, planets))
    print("\n".join(map(str, result)))

if __name__ == '__main__':
    main()