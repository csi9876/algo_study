import sys
sys.stdin = open('input.txt')

import sys
# from collections import deque
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
M = int(input())
box = list(map(int, input().split()))
box.sort(reverse=True)
# box = deque(box)
# print(N, M)
# print(arr)
# print(box)
res = 0
if arr[0] < box[0]:
    res = -1
else:
    while box:
        # print(arr)
        # print(box)
        for i in range(len(arr)):
            for j in range(len(box)):
                # print(i)
                if arr[i] >= box[j]:
                    box.pop(j)
                    break
                else:
                    pass
        res += 1
print(res)

