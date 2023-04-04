import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

arr = []
while True:
    try:
        a = int(input())
        arr.append(a)
    except:
        break
# print(arr)

def postorder(s, e):
    if s > e:
        return
    mid = e + 1
    for i in range(s + 1, e + 1):
        if arr[s] < arr[i]:
            mid = i
            break

    postorder(s + 1, mid - 1)
    postorder(mid, e)
    print(arr[s])

postorder(0, len(arr) - 1)