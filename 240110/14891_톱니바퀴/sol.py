import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


# 더미 바퀴
arr = [[0, 0, 0, 0, 0, 0, 0, 0]]
score = [1, 2, 4, 8]
result = 0

for _ in range(4):
    temp = list(map(int, input().strip()))
    arr.append(temp)

k = int(input())
for i in range(k):
    num, t = map(int, input().split())
    # left

    # 회전 여부 저장
    turn = [0] * 5
    turn[num] = t

    # 왼쪽 톱니바퀴 확인 및 회전 방향 결정
    a, b = num - 1, num  # a 는 왼쪽 바퀴, b는 오른쪽 바퀴
    while a > 0:    # 왼쪽 끝까지 확인
        if arr[a][2] != arr[b][6]:  # 맞닿은 톱니가 다르면
            turn[a] = turn[b] * -1  # 반대방향으로 회전
        else:
            break
        a, b = a - 1, b - 1

    # 오른쪽 톱니바퀴 확인 및 회전 방향 결정
    a, b = num, num + 1
    while b < 5:    # 오른쪽 끝가지 확인
        if arr[a][2] != arr[b][6]:  # 맞닿은 톱니가 다르면
            turn[b] = turn[a] * -1  # 반대로 회전
        else:
            break
        a, b = a + 1, b + 1

    # 결정된 회전 방향에 따른 톱니 회전
    for i in range(1, 5):
        if turn[i] == 1:    # 시계 방향 회전
            temp = arr[i][7]
            arr[i][1:8] = arr[i][0:7]
            arr[i][0] = temp

        if turn[i] == -1:   # 반시계 방향 회전
            temp = arr[i][0]
            arr[i][0:7] = arr[i][1:8]
            arr[i][7] = temp

for i in range(4):
    # 점수 추가
    result += arr[i + 1][0] * score[i]

print(result)