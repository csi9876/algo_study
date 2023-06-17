import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
t = input().strip()
# print(a, b)

res = 0
try:
    while t != s:
        if t == s:
            res = 1
            break
        if len(t) == 0:
            pass
        if t[-1] == 'A':
            t = t[:-1]
        elif t[-1] == 'B':
            t = t[::-1]
            t = t[1:]
        else:
            pass
    res = 1
except:
    res = 0

print(res)