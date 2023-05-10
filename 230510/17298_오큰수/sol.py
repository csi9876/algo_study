import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
que = list(map(int, input().split()))
result = []
res = [-1] * N
# print(que)
maxn = que[0]+1
for i in range(N):
    if que[i] <= maxn:
        result.append(i)
        maxn = que[i]
    if maxn < que[i]:
        while len(result) >= 1 and que[result[-1]] < que[i]:
            res[result.pop()] = que[i]
        result.append(i)
print(*res)


# result = []
# for i in range(N):
#     for j in range(i, N):
#         if que[i] < que[j]:
#             result.append(que[j])
#             break
#     else:
#         result.append(-1)
# print(*result)