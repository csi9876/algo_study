import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
bit = [0] * Q
stack = set()

for i in range(Q):
    a = int(input())
    temp = a

    while temp > 0:
        if temp in stack:
            bit[i] = temp
        temp//=2

    if bit[i] == 0:
        stack.add(a)
    print(bit[i])