import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 8)

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])     # 부모 찾기 위해 재귀
    return parent[x]    # 부모 노드 반환


def union(x, y):
    x, y = find(x), find(y)  # 각각 부모

    if x == y:  # 같은 그룹이면 반환
        return child[x]

    parent[y] = x   # y부모를 x로
    child[x] += child[y]    # x 그룹 원소 + y 그룹 원소
    return child[x]


n, m = map(int, input().split())
parent = [i for i in range(n)]
child = [0 for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        break
    union(a, b)
else:
    print(0)
