import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())

def solve():
    for i in range(10000, 100000):
        j = n - i
        i = str(i)
        j = str(j)

        if len(j) == 5 and i[2] == i[3] == j[3] and i[4] == j[1] and len(set(i+j)) == 7:
            if n < 100000:
                print("  ", i, sep="")
                print("+ ", j, sep="")
                print("-------")
                print("  ", n, sep="")
                return
            else:
                print("  ", i, sep="")
                print("+ ", j, sep="")
                print("-------")
                print(" ", n, sep="")
                return
    print("No Answer")

solve()