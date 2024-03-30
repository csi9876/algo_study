import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    s = input().strip()
    if s[0:3] == "pus":
        s, e = s.split()
        stack.append(int(e))

    elif s[0:3] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif s[0:3] == "siz":
        print(len(stack))

    elif s[0:3] == "emp":
        if stack:
            print(0)
        else:
            print(1)

    elif s[0:3] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)