import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
res = []
stack = []

while arr:
    index = len(arr)
    temp = arr.pop()
    if stack and stack[0] < temp:
        res.append(index)
        stack.pop(0)
        stack.append(temp)
    else:
        stack.append(temp)

print(arr)
print(stack)
print(res)
