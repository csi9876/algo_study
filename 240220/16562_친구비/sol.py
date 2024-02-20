import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
parent = list(i for i in range(n + 1))
child = list(map(int, input().split()))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x, y = find(x), find(y)
    # 친구비를 기준으로 부모 설정
    if child[x] < child[y]:
        parent[y] = x
    else:
        parent[x] = y

for _ in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

res = set()
cost = 0

# parent 친구의 요금의 총합
for i in range(n):
    if find(i) not in res:
        cost += child[parent[i]]
        res.add(parent[i])
if cost > k:
    print("Oh no")
else:
    print(cost)


