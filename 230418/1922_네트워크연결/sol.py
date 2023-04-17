import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

v = int(input())
e = int(input())
adj =[]
pare = [i for i in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())

    adj.append([a, b, c])


def find(x):
    # 초기 x를 포함하는 집합의 대표노드 찾기
    # x가 자기 자신을 부모로 가질 때 까지 타고 올라감
    # while x != pare[x]:
    #     x = pare[x]
    # return x

    # if x != pare[x]:
    #     x = find(pare[x])
    # return x

    if x != pare[x]:
        # pare[x] = find(pare[x])
        pare[x] = find(pare[x])
    return pare[x]


def union(x, y):
    # 결합하며:  y를 포함하는 집합의 대표노드의 부모 = x를 포함하는 집단의 대표노드로 설정
    if find(y) > find(x):
        pare[find(y)] = find(x)
    elif find(y) < find(x):
        pare[find(x)] = find(y)

adj.sort(key=lambda x:x[2])
sumn = 0
cnt = 0
mst = []


for a, b, w in adj:
    # 사이클이 존재하면 다음 간선으로 바로 이동
    # 부모노드 비교 서로 같은 대표노드면 사이클

    # 사이클이 존재하지 않으면 (서로 속한 집합의 대표노드가 다르면)
    if find(a) != find(b):
        # 순회 횟수 +1
        cnt += 1

        # 가중치의 합에 + 가중치
        sumn += w

        # MST 배열에 간선 추가
        mst.append([a, b, w])

        # 노드 b, a 결합
        union(a, b)

        # 노드 수 -1 만큼의 간선을 다 순회하면 종료
        if cnt == v:
            break
# print(pare)
print(sumn)  # 간선 가중치의 합
# print(mst)
# print(arr)


