import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
r = r-1
c = c-1

time = 0
res = - 1

while time < 100:
    if arr[r][c] == k:
        res += 1
        break

    if len(arr) >= len(arr[0]):
        print(1)
    else:
        print(0)

    time += 1

print(res)


'''



'''

