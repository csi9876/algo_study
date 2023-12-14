import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = []
for _ in range(n):
    s, e = map(int, input().split())
    arr.append((s,e))
arr.sort()
que = []
que.append(arr[0][1])   # 첫 원소

for i in range(1, n):   # 순서대로 돌리기
    s, e = arr[i][0], arr[i][1]
    finish = que[0]  # 가장 작은 회의 끝나는 시간
    if finish > s:  # 새로운 회의실 사용해야 하는 경우
        heapq.heappush(que, e)
    else:       # 같은 회의실 이어서 사용하는 경우
        heapq.heapreplace(que, e)
print(len(que))