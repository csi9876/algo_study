import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

res = 0

for i in range(n):
    max_n = 0
    l = int(1e9)    # 왼쪽의 기울기 최솟값
    r = -int(1e9)    # 오른쪽 기울기 최댓값

    for j in range(i-1, -1, -1):    # 왼쪽
        temp = (arr[j]-arr[i])/((j+1)-(i+1))
        if temp < l:    # 기울기가 더 작다면
            l = temp
            max_n += 1
    for j in range(i+1, n):  # 오른쪽
        temp = (arr[j]-arr[i])/((j+1)-(i+1))
        if temp > r:    # 기울기가 더 크다면
            r = temp
            max_n += 1
    res = max(res, max_n)
print(res)