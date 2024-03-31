import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 능력치 차이
def cal(team):
    a, b = 0, 0
    for i in range(n):
        for j in range(n):
            if team[i] and team[j]:
                a += arr[i][j]
            elif not team[i] and not team[j]:
                b += arr[i][j]
    return abs(a - b)

# 백트래킹
def solve(idx, team, cnt):
    if cnt == n // 2:
        global ans
        ans = min(ans, cal(team))
        return
    if idx >= n:
        return

    team[idx] = True    # 해당 인덱스 a 팀
    solve(idx + 1, team, cnt + 1)

    team[idx] = False   # 해당 인덱스 b 팀
    solve(idx + 1, team, cnt)

ans = sys.maxsize
solve(0, [False] * n, 0)
print(ans)