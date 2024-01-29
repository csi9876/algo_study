import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
m = int(input())
arr = []
for i in range(1, m + 1):
    t = int(input())
    arr.append((t, i))  # 먹는 시간과 사람 번호 같이 저장

def solve(arr):
    sum_v = 0   # 소보루 먹는 숫자
    time = 0    # 총 시간

    while True:
        for t, idx in arr:  # 각 사람 시간과 번호
            if time % t == 0:  # 현재 시간 % 소보루 먹는 시간
                sum_v += 1  # 소보루를 먹기
                if sum_v == n - s:  # 전체 - 남은 소보루 == 여태 먹은 소보루 면
                    return idx  # 마지막으로 먹은 사람이므로 해당 번호를 반환
        time += 1  # 시간 증가

print(solve(arr))  # 마지막으로 소보루를 먹은 사람
