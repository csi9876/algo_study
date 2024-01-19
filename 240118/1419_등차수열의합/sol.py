import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline



l = int(input())
r = int(input())
k = int(input())

cnt = 0

# 분기 처리
if k == 2:  # 3이상의 수 중에서 2의 배수의 개수
    min_n = max(l, 3)
    cnt = (r - min_n + 1) if r >= min_n else 0
elif k == 3:  # k가 3인 경우, 6 이상의 수 중에서 3의 배수의 개수
    min_n = max((l + 2) // 3, 2)
    max_n = r // 3
    cnt = max_n - min_n + 1 if max_n >= min_n else 0
elif k == 4:    # k가 4인 경우, 10 이상의 수 중에서 2의 배수이지만 12가 아닌 수의 개수
    min_n = max((l + 1) // 2, 5)
    max_n = r // 2
    cnt = max_n - min_n + 1 if max_n >= min_n else 0
    if 6 >= min_n and 6 <= max_n:
        cnt -= 1
elif k == 5:    # k가 5인 경우, 15 이상의 수 중에서 5의 배수의 개수
    min_n = max((l + 4) // 5, 3)
    max_n = r // 5
    cnt = max_n - min_n + 1 if max_n >= min_n else 0

print(cnt)

'''
123 = 6
135 = 9
147 = 12
234 = 9
246 = 12
345 = 12
'''
