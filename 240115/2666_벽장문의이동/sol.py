import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
s1, s2 = map(int, input().split())
m = int(input())
arr = list(int(input()) for _ in range(m))


