import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
res = [0 * N]
stack = []

while arr:
    for n, i in stack:
        for j in range(len(arr), 0, -1):
            if n == arr[j]:
                res[i] = arr[j]
    if not stack:
        stack.append(arr.pop())


# while arr:
#     index = len(arr)
#     temp = arr.pop()
#     if stack and stack[0] < temp:
#         res.append(index)
#         stack.pop(0)
#         stack.append(temp)
#     else:
#         stack.append(temp)
#
print(arr)
print(stack)
print(res)
