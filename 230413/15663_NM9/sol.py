import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []
v = [0]*(N+1)

def bt(n, lst):
    if n == M:
        print(*lst)
        return

    temp = 0
    for i in range(N):
        if v[i] == 0 and temp!=arr[i]:
            temp = arr[i]
            v[i] = 1
            bt(n+1, lst+[arr[i]])
            v[i] = 0

bt(0, [])