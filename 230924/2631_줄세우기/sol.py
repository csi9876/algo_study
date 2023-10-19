import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


def solution(lines):
    dp = [1]*len(lines)
    for i in range(len(lines)):
        for j in range(i):
           if lines[i] > lines[j]:
               dp[i] = max(dp[i], dp[j]+1)
    return len(lines)-max(dp)

arr = []
for i in range(int(input())):
    arr.append(int(input()))

print(solution(arr))
