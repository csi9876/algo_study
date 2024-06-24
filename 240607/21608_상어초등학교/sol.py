import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

'''
(r,c) 좌표
좌상단 1,1 우하단 n,n
학생 순서 + 좋아하는 학생 4명 리스트
|r1-r2| + |c1-c2| = 1 이면 인접

앉기 규칙
1. 빈 칸 중 좋아하는 학생이 가장 많이 인접한 칸에 앉는다
2. > 빈 칸이 가장 많이 인접한 칸에 앉는다
3. > 행이 가장 작은 칸 > 열이 가장 작은 칸

'''


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n**2)]


def bfs():
    for i in range(n):
        for j in range(n):
            if