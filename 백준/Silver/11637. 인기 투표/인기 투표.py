import sys
input = sys.stdin.readline

def find_winner():
    T = int(input().strip())

    for _ in range(T):
        n = int(input().strip())
        votes = [int(input().strip()) for _ in range(n)]
        total_votes = sum(votes)
        max_votes = max(votes)
        max_count = votes.count(max_votes)
        winner_index = votes.index(max_votes) + 1

        if max_count > 1:
            print("no winner")
        elif max_votes > total_votes // 2:
            print(f"majority winner {winner_index}")
        else:
            print(f"minority winner {winner_index}")

if __name__ == '__main__':
    find_winner()