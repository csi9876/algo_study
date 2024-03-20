import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
arr = []
for num in range(n):
    p, f, s, v, c = map(int, input().split())
    arr.append((p, f, s, v, c, num + 1))

min_cost = int(1e9)
res = []

def solve(idx, sp, sf, ss, sv, sc, lst):
    global min_cost, res

    # 영양분 모두 만족하면
    if sp >= mp and sf >= mf and ss >= ms and sv >= mv:
        if sc < min_cost:   # 최저 비용 갱신
            min_cost = sc
            res = lst
        elif sc == min_cost:    # 최저 비용과 동일
            res = min(res, lst)
        return

    # 모든 재료 순회 or 비용 오버
    if idx == n or sc > min_cost:
        return

    solve(idx + 1, sp, sf, ss, sv, sc, lst)  # 현재 재료를 선택하지 않는 경우
    solve(idx + 1, sp + arr[idx][0], sf + arr[idx][1], ss + arr[idx][2], sv + arr[idx][3], sc + arr[idx][4], lst + [arr[idx][5]])  # 현재 재료를 선택하는 경우

# idx, sp, sf, ss, sv, sc ,lst
solve(0, 0, 0, 0, 0, 0, [])

if min_cost == int(1e9):
    print(-1)
else:
    print(min_cost)
    print(' '.join(map(str, sorted(res))))