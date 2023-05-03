import sys
sys.stdin = open('input.txt')

from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
k = int(input())
# print(N)
arr = []
for i in range(N):
    for j in range(N):
        if len(arr) > k and (i+1)*(j+1) > arr[-1]:
            continue
        # arr.append((i+1)*(j+1))
        idx = bisect_left(arr, (i+1)*(j+1))
        arr = arr[:idx] +[(i+1)*(j+1)] +  arr[idx:]
        if idx == k:
            break

print(arr[k])

# print(adj)