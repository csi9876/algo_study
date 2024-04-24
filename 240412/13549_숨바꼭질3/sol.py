import sys
sys.stdin = open('input.txt')

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())


max_n = 100001
v = [False]*max_n
cnt = 0
que = deque()

que.append((n, cnt))
v[n] = True

while que:
  cur, cnt = que.popleft()
  v[cur] = True  # 현재 위치를 방문 처리

  if cur == k:
    print(cnt)
    break

  for next in (cur * 2, cur + 1, cur - 1):
      if 0 <= next < max_n and not v[next]:
          if next == cur * 2:
              que.appendleft((next, cnt))  # 2배 증가하는 경우는 시간이 증가하지 않으므로 count 그대로
          else:
              que.append((next, cnt + 1))
