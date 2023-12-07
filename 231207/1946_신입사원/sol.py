import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        score, rank = map(int, input().split())
        arr.append([score, rank])
    # 서류 성적 순으로 정렬
    arr.sort()

    # 면접 성적 최고 순위 기록
    minn = int(1e9)
    cnt = 0
    for score, rank in arr:
        # 면접 순위가 현재 최고 순위보다 좋으면 cnt +1 / 최고순위 교체
        if rank < minn:
            cnt += 1
            minn = rank
    print(cnt)
