import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()      # 시작 순 정렬, 종료 순 정렬

room = []   # 사용 회의실
heapq.heappush(room, arr[0][1])  # 첫 회의실 = 가장 빠른 종료 시각

for i in range(1, n):
    # 현재 회의 끝 보다 다음 회의 시작이 빠르면
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])  # 새 회의실
    else:   # 현재 회의 끝나면 비우고 다음 회의 넣기
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])

print(len(room))