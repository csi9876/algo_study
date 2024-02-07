import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())

# 별 배열 설정
arr = [[' '] * 2 * n for _ in range(n)]

def solve(x, y, size):
    # 3일 경우 직접 그리기
    if size == 3:
        arr[x][y] = '*'
        arr[x + 1][y - 1] = arr[x + 1][y + 1] = "*"
        for k in range(-2, 3):
            arr[x + 2][y - k] = "*"
    else:   # 아니면 반 나눠가며 재귀 호출 / 3의 반복
        ns = size//2
        solve(x, y, ns)
        solve(x + ns, y - ns, ns)
        solve(x + ns, y + ns, ns)

#  최상단 x, y, 크기
solve(0, n - 1, n)
for i in arr:
    print("".join(i))