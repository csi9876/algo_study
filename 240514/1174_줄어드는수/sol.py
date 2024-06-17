import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
res = set()
num = []

def dfs():
    if num:
        res.add((int(''.join(map(str, num)))))

    for i in range(10):
        if not num or num[-1] > i:  # num이 없거나 감소하는 수면
            num.append(i)   # 추가하고 반복
            dfs()
            num.pop()

dfs()
res = sorted(res)
if len(res) >= n:
    print(res[n-1])
else:
    print(-1)

'''
0
1
2
3
4

5
6
7
8
9

10
20
21
30
31

32
40
41
42
'''
