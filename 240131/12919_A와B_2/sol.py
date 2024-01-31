import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()

def solve(t):
    if t == s:
        print(1)
        sys.exit()

    if len(t) == 0:
        return 0

    if t[-1] =='A':  # 마지막이 A면 제거
        solve(t[:-1])

    if t[0] == 'B':     # 처음이 B면 제거하고 뒤집기
        solve(t[1:][::-1])

solve(t)
print(0)