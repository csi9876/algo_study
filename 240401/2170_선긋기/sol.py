import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = sorted(list(map(int, input().split())) for _ in range(n))

start = arr[0][0]
end = arr[0][1]
res = 0
for s, e in arr:
    if end < s:
        res += end-start
        start, end = s, e
        continue
    end = max(end, e)
res += end-start
print(res)
