import sys
sys.stdin = open('input.txt')

arr1 = ['a']+ list(input())
arr2 = ['a']+list(input())
k = max(len(arr1), len(arr2))
# print(arr1)
# print(arr2)

v = [[0]*(k) for _ in range(k)]
# for i in v:
#     print(i)

for i in range(1, len(arr1)):
    for j in range(1, len(arr2)):
        if arr1[i] == arr2[j]:
            v[i][j] = v[i-1][j-1]+1
        else:
            v[i][j] = max(v[i - 1][j], v[i][j - 1])

maxn = 0
for i in v:
    for j in i:
        maxn = max(maxn, j)
print(maxn)