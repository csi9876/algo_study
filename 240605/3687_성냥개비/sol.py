import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline

t = int(input())

# 0~10 성냥개비로 만들 수 있는 최소 숫자들
nums = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]


def getMax(n):
    ret = [1 for _ in range(n // 2)]
    if n & 1:
        ret[0] = 7
    return ret


def getMin(n):
    ret = [8 for _ in range((n + 6) // 7)]
    if n % 7 == 1:
        ret[0] = 1
        ret[1] = 0
    if n % 7 == 2:
        ret[0] = 1
    if n % 7 == 3:
        ret[0] = 2
        ret[1] = 0
        ret[2] = 0
    if n % 7 == 4:
        ret[0] = 2
        ret[1] = 0
    if n % 7 == 5:
        ret[0] = 2
    if n % 7 == 6:
        ret[0] = 6
    return ret

for _ in range(t):
    n = int(input())
    if n < 11:
        print(nums[n], end=" ")
    else:
        print(*getMin(n), sep='', end=' ')
    print(*getMax(n), sep='')


'''
2 : 1, 1
3 : 7, 7
4 : 4, 11
5 : 2, 71
6 : 6, 111
7 : 8, 711
8 : 10, 771

'''
