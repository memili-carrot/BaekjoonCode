import sys
input = sys.stdin.readline

def junhee():
    n = int(input())
    votes = [int(input()) for _ in range(n)]

    if votes.count(1) > votes.count(0):
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")

if __name__ == '__main__':
    junhee()