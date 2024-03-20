import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = []

for i in range(n):
    d, c = map(int, input().split())
    arr.append((d, c))
arr.sort(key=lambda x: (x[0], -x[1]))
# print(arr)

que = []
for d, c in arr:
    # 현재 작업을 추가
    heapq.heappush(que, c)
    print(que)

    # 큐의 크기가 현재 마감일 보다 크면 완료할 수 없는 작업이므로 제거
    if len(que) > d:
        heapq.heappop(que)

print(sum(que))