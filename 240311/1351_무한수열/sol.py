import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, p, q = map(int, input().split())

# 이미 나온 숫자 기억
arr = {0 : 1}

def solve(x, p, q, arr):
    if x in arr:
        return arr[x]

    # ai = a[i/pj] + a[i/qj]
    arr[x] = solve(x//p, p, q, arr) + solve(x//q, p, q, arr)
    return arr[x]

print(solve(n, p, q, arr))