import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


def dfs(index, arr):
    # 모든 인덱스가 처리된 경우
    if index == len(kriii):
        print(*arr)
        exit()

    # 1자리 수 처리
    num1 = int(kriii[index])  # 현재 인덱스의 1자리 수
    if num1 <= N and not visited[num1]:  # N을 체크하여 범위 초과 방지
        visited[num1] = True
        arr.append(num1)  # 재귀 호출
        dfs(index + 1, arr)
        visited[num1] = False
        arr.pop()

    # 2자리 수 처리
    if index + 1 < len(kriii):  # 다음 인덱스가 범위 내에 있는지 확인
        num2 = int(kriii[index:index + 2])  # 현재 인덱스의 2자리 수
        if num2 <= N and not visited[num2]:  # N을 체크하여 범위 초과 방지
            visited[num2] = True
            arr.append(num2)  # 2칸 건너 재귀 호출
            dfs(index + 2, arr)
            visited[num2] = False
            arr.pop()

kriii = input().strip()
N = len(kriii) if len(kriii) < 10 else 9 + (len(kriii) - 9) // 2
visited = [0 for _ in range(N + 1)]  # visited 배열 초기화

dfs(0, [])