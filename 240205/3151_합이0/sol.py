import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0

def solve(s,e,g):
    global res
    max_idx = n
    while s < e:
        temp = arr[s] + arr[e]
        if temp < g:
            s += 1
        elif temp == g:
            if arr[s] == arr[e]:
                res += e-s
            else:
                if max_idx > e:
                    max_idx = e
                    while max_idx > s and arr[max_idx-1] == arr[e]:
                        max_idx -= 1
                res += e - max_idx + 1
            s += 1
        else:
            e -= 1



for i in range(n - 2):
    s = i + 1
    e = n - 1
    goal = -arr[i]
    solve(s, e, goal)
print(res)