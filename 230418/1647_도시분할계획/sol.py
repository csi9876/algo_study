import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
adj =[]
pare = [i for i in range(v+1)]
result = []
for _ in range(e):
    a, b, c = map(int, input().split())
    adj.append([a, b, c])

def find(x):
    if x != pare[x]:
        pare[x] = find(pare[x])
    return pare[x]


def union(x, y):
    if find(y) > find(x):
        pare[find(y)] = find(x)
    elif find(y) < find(x):
        pare[find(x)] = find(y)

adj.sort(key=lambda x:x[2])
cnt = 0

for a, b, w in adj:
    if find(a) != find(b):
        cnt += 1
        union(a, b)
        result.append(w)
        if cnt == v:
            break

print(sum(result[:-1]))



