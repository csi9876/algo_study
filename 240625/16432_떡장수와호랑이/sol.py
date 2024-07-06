import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
day = []
res = []

for _ in range(n):
    m, *arr = map(int, input().split())
    day.append(arr)

# v[i][d-1]는 i번째 날에 d 숫자를 사용했는지 여부를 나타냄
v = {i: [0 for _ in range(10)] for i in range(n+1)}

def dfs(cnt, arr, prev):
    # 모든 날에 대해 숫자를 선택한 경우
    if cnt == n:
        for d in arr:
            print(d)
        exit()  # 프로그램 종료

    # 현재 날에 대해 가능한 숫자들을 순회
    for d in day[cnt]:
        if d != prev and not v[cnt][d-1]:  # 이전 숫자와 다르고 방문하지 않은 숫자인 경우
            v[cnt][d-1] = 1  # 숫자 d를 사용했음을 표시
            dfs(cnt+1, arr+[d], d)  # 다음 날에 대해 재귀 호출
            # 백트래킹을 위해 v[cnt][d-1]을 0으로 되돌리지 않는 이유:
            # exit()로 인해 성공적인 경우 프로그램이 종료되기 때문

# DFS 탐색 시작
dfs(0, [], 0)

# 가능한 숫자 배열을 찾지 못한 경우 -1 출력
print(-1)