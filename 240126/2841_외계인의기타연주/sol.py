import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n, p = map(int, input().split())
v = [[0] for _ in range(7)]     # 기타 1~6번 줄
cnt = 0

for i in range(n):
    line, plat = map(int, input().split())

    # 현재 플랫 높이가 현재 줄의 마지막 플랫 높이보다 클때까지
    # 마지막 플랫 삭제 및 cnt +1
    while v[line][-1] > plat:
        v[line].pop()
        cnt += 1

    # 현재 플랫과 현재 줄 마지막 플랫의 높이가 같다면
    # 패스
    if v[line][-1] == plat:
        continue

    # 현재 줄에 입력받은 플랫 추가
    # cnt +1
    v[line].append(plat)
    cnt += 1

print(cnt)