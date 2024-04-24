import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split(' ')))
code = []
res = 0

for now in range(k):
    if arr[now] in code:    # 이미 멀티탭에 꽂혀있음
        continue

    if len(code) < n:  # 멀티탭 자리 남음
        code.append(arr[now])
        continue

    idx = []
    for c in code:   # 꽂혀져 있는 코드들
        if c in arr[now:]:   # 다음에 또 이용해야한다면
            idx.append(arr[now:].index(c))
        else:
            idx.append(101)
    temp = idx.index(max(idx))
    code.remove(code[temp])
    code.append(arr[now])
    res += 1

print(res)