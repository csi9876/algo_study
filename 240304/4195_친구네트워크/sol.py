import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # 부모 찾기 위해 재귀
    return parent[x]    # 부모 노드 반환


def union(x, y):
    x, y = find(x), find(y)  # 각각 부모
    if x == y:  # 같은 그룹이면 반환
        return child[x]

    parent[y] = x   # y부모를 x로
    child[x] += child[y]    # x 그룹 원소 + y 그룹 원소
    return child[x]


t = int(input())
for _ in range(t):
    child = dict()
    parent = dict()

    for _ in range(int(input())):
        a, b = input().split()

        if not child.get(a):    # 처음 등장한 거면
            parent[a] = a   # 자신이 자신의 부모
            child[a] = 1    # 자식 1개

        if not child.get(b):
            parent[b] = b
            child[b] = 1

        print(union(a, b))
