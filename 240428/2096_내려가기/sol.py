import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
a, b, c = map(int, input().split())

dp_min = [a, b, c]
dp_max = [a, b, c]

for i in range(1, n):
        a, b, c = map(int, input().split())
        # 최솟값
        x, y, z = dp_min
        dp_min[0] = a + min(x, y)
        dp_min[1] = b + min(x, y, z)
        dp_min[2] = c + min(y, z)

        # 최댓값
        x, y, z = dp_max
        dp_max[0] = a + max(x, y)
        dp_max[1] = b + max(x, y, z)
        dp_max[2] = c + max(y, z)


print(max(dp_max), min(dp_min))