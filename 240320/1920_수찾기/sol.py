import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
lstN = list(map(int, input().split()))
lstN.sort()

m = int(input())
lstM = list(map(int, input().split()))

for i in lstM:
    s = 0
    e = n - 1
    flag = 0

    while s <= e:
        mid = (s + e) // 2
        if lstN[mid] == i:
            print(1)
            flag = 1
            break
        if i > lstN[mid]:
            s = mid + 1
        else:
            e = mid - 1

    if flag == 0:
        print(0)

