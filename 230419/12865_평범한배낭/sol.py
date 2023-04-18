import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
arr = [(0,0)]
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W,V))
# print(arr)
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    # 한계 무게를 1부터 올라오면서 순회
    for j in range(1, K+1):
        w, v = arr[i]
        # print(w,v)
        # 가방에 넣을 수 있으면
        if j >= w:
            # 전 값 vs 현재 가치 + 이전 물건의 현재 무게-현재 무게
            # print(dp)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            # 넣을 수 없으면 전 값을 가져오기
            dp[i][j] = dp[i-1][j]
        print(dp)
# print(dp)
print(dp[i][K])