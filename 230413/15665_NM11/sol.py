import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []
def bt(n, lst):
    if n == M:
        print(*lst)
        return

    temp = 0
    for i in range(N):
        if temp!=arr[i]:
            temp = arr[i]
            bt(n+1, lst+[arr[i]])

bt(0, [])