import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
arr = list(input().strip())
count = [0] * 26    # 알파벳 개수
size = len(arr)

s = 0
e = 0

cnt = 0     # 윈도우에 있는 서로 다른 알파벳 개수
que = deque()  # 알파벳 저장
res = 0

while s < size and e < size:
    while e < size:
        # 현재 윈도우에 있는 서로 다른 알파벳의 개수가 n이고, 새로운 알파벳이 이미 윈도우에 없는 경우
        if cnt == n and not count[ord(arr[e]) - ord('a')]:
            break

        # 새로운 알파벳이 윈도우에 없는 경우
        if not count[ord(arr[e]) - ord('a')]:
            cnt += 1
        count[ord(arr[e]) - ord('a')] += 1
        que.append(arr[e])
        e += 1

    res = max(res, len(que))
    temp = que[0]       # que의 첫번째 알파벳
    count[ord(temp) - ord('a')] -= 1
    que.popleft()
    if not count[ord(temp) - ord('a')]:
        cnt -= 1
    s += 1

print(res)
