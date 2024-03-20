import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

if n <= k:
    print(0)
else:
    arr.sort()
    minus = []

    for i in range(n-1):
        # 다음 지점과 거리, 현 위치, 다음 위치
        minus.append((arr[i+1] - arr[i], i, i+1))

    # 거리 긴 순
    minus.sort(reverse=True)

    roca = []
    for i in range(k-1):
        # 끊어질 현위치와 다음위치 k개 저장
        roca.append((minus[i][1], minus[i][2]))

    s = arr[0]      # 시작 지점 첫위치
    e = arr[-1]     # 끝 지점 마지막 위치
    res = 0

    for i in range(len(roca)):
        res += arr[roca[i][0]] - s  # 현재 구간 거리 추가
        s = arr[roca[i][1]]     # 다음 구간 시작 위치 업데이트

    res += e - s    # 마지막 구간 거리 추가
    print(res)


