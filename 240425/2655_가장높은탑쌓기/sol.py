import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip().split())) for i in range(n)]
