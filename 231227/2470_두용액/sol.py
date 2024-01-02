import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = n-1

ans = 1000000000 * 2
res = []

while l < r:
    temp_l = arr[l]
    temp_r = arr[r]
    temp = temp_l + temp_r

    if abs(temp) < ans:
        ans = abs(temp)
        res = [temp_l, temp_r]

    if temp < 0:
        l += 1
    else:
        r -= 1
print(*res)