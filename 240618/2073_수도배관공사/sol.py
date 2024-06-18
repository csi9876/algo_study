import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# 수도관 설치 d 거리 떨어진 곳 연결
# 파이프를 일렬로 연결해 수도관
# 용량은 파이프 용량 최소값
# 길이는 파이프 길이 총합
# 수도관 길이는 정확히 D

d, p = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(p)]


# dp[i]: 길이 i의 수도관을 만들 때의 최대 용량
dp = [0] * (d + 1)
dp[0] = int(1e9)  # 초기값 큰 값 설정

# 주어진 파이프들을 하나씩 확인
for l, c in arr:
    # 파이프를 연결할 수 있는 모든 경우를 역순으로 탐색
    for i in range(d, l - 1, -1):
        if dp[i - l]:
            dp[i] = max(dp[i], min(dp[i - l], c))

# 길이가 정확히 d인 수도관의 최대 용량을 출력
print(dp[d])