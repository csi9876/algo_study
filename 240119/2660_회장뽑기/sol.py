import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

inf = sys.maxsize

n = int(input())
arr = [[inf] * n for _ in range(n)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1

for i in range(n):
    arr[i][i] = 0

# 플루이드 워셜 최단거리 탐색
for k in range(n):  # 거쳐가는 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            # 최단거리면 교체
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

res = []
min_n = inf
min_arr = []

# 최소 거리찾고 해당 정점들 리스트업
for i in range(n):
    if min_n > max(arr[i]):
        min_n = max(arr[i])
        min_arr = [i + 1]
    elif min_n == max(arr[i]):
        min_arr.append(i + 1)
    else:
        continue

print(min_n, len(min_arr))
print(*min_arr)