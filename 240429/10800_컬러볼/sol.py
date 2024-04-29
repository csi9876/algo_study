import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# 자기 공보다 크기 작고, 색이 다른 공 잡기
# 잡을 수 있는 공의 크기의 합
n = int(input())
arr = []

res = [0] * (n + 1)     # 잡은 공 결과
color = [0] * (n + 1)   # 색깔 별 누적 크기
weight = [0] * 2001     # 무게 별 누적 크기

for i in range(n):
        c, s = map(int, input().split())
        arr.append((s, c, i))

arr.sort()

prefix_sum = [0] * (n + 1)      # 누적합
for i in range(0, n):
        # 현재 공까지 누적합
        prefix_sum[i] = prefix_sum[i - 1] + arr[i][0]

        # 이전 공과 색깔 크기 같으면 이전 값
        if i > 0 and arr[i][1] == arr[i - 1][1] and arr[i][0] == arr[i - 1][0]:
                res[arr[i][2]] = res[arr[i - 1][2]]
        else:   # 아니면 계산
                res[arr[i][2]] = prefix_sum[i - 1] - color[arr[i][1]] - weight[arr[i][0]]

        # 색깔과 크기별 누적 크기 업데이트
        color[arr[i][1]] += arr[i][0]
        weight[arr[i][0]] += arr[i][0]

for i in range(0, n):
        print(res[i])
