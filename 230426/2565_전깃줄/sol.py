import sys
sys.stdin = open('input.txt')

N = int(input())
arr1=[0]
arr2=[0]
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()
for a, b in arr:
    arr1.append(a)
    arr2.append(b)
# print(arr1)
# print(arr2)
dp1 = [0] * (N+1)
dp2 = [0]* (N+1)
# 1~N까지
for i in range(1, N+1):
    maxn = 0
    maxn1 = 0
    # 0번째에서 i번째 까지
    for j in range(0, i):
        if arr1[i] > arr1[j] and arr2[i] > arr2[j]:
            maxn = max(maxn, dp1[j]+1)
            maxn1 = max(maxn, dp2[j]+1)
    dp1[i] = maxn
    dp2[i] = maxn1

# print(dp1)
# print(dp2)
result = max(dp1)
print(N-result)