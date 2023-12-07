import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from collections import deque

t = int(input())

for i in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(",")
    que = deque(arr)

    rev, front, back = 0, 0, len(que)-1
    flag = 0
    if n == 0:
        que = []
        front = 0
        back = 0

    for j in p:
        if j == 'R':
            rev += 1
        elif j == 'D':
            if len(que) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
    if flag == 0:
        if rev % 2 == 0:
            print("[" + ",".join(que) + "]")
        else:
            que.reverse()
            print("[" + ",".join(que) + "]")