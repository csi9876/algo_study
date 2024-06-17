import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

# 좌, 우 순서로 미네랄 파괴
# 미네랄 파괴하면 중지
# 파괴 후 클러스터 발생
# 바닥까지 이동
# 미네랄 만날때 까지 이동

r, c = map(int, input().split())
cave = [list(input().strip()) for _ in range(r)]
n = int(input())
sticks = [int(x) for x in input().split()]

