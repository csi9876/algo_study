import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


N = int(input())
for i in range(1, N+1):
    print((N-i)*" "+"*"*i)