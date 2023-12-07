import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n, k = map(int, input().split())

res = 0
temp = bin(n).count('1')

while temp > k:
    n += 1
    res += 1
    temp = bin(n).count('1')

print(res)