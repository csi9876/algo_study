import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

res = 0

# 오른쪽 아래부터 역인덱싱
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if arr[i][j] == 1:
            res += 1

            # 범위 뒤집기
            for x in range(i+1):
                for y in range(j+1):
                    if arr[x][y] == 1:
                        arr[x][y] = 0
                    else:
                        arr[x][y] = 1
print(res)