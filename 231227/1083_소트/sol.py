import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(n-1):    # 처음 ~ n-1
    mx = arr[i]     # 현재 원소를 최대값으로 설정
    idx = i     # 현재 idx

    # 현재 원소의 다음 원소 ~ 교환 가능한 범위 내의 원소들 순회
    for j in range(i+1, min(n, i+1+s)):
        if mx < arr[j]:     # 순회중인 원소가 현재 최대값보다 크면
            mx = arr[j]     # 새로운 최대값으로 변경
            idx = j     # 그 원소의 인덱스를 idx로 설정
    s -= (idx-i)     # 교환한 횟수 s에서 감소

    # idx ~ i 까지 역순 순회
    for j in range(idx, i, -1):
        arr[j] = arr[j-1]   # 순회 중인 원소를 그 앞의 원소로 대체
    arr[i] = mx  # i번째 원소를 최대값으로 대체

print(*arr)
