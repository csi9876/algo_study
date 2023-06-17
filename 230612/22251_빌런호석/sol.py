import sys
sys.stdin = open('input.txt')

N, K, P, X = map(int, input().split())
# n : 1~n 층
# k : 디스플레이 자리의 수
# p : 최소1 ~ 최대 p 개 반전
# x : 현재 머무르는 층

arr = {'0':[1, 1, 1, 0, 1, 1, 1],
        '1':[0, 0, 1, 0, 0, 1, 0],
        '2':[1, 0, 1, 1, 1, 0, 1],
        '3':[1, 0, 1, 1, 0, 1, 1],
        '4':[0, 1, 1, 1, 0, 1, 0],
        '5':[1, 1, 0, 1, 0, 1, 1],
        '6':[1, 1, 0, 1, 1, 1, 1],
        '7':[1, 0, 1, 0, 0, 1, 0],
        '8':[1, 1, 1, 1, 1, 1, 1],
        '9':[1, 1, 1, 1, 0, 1, 1]
       }

X = str(X).zfill(K)
# print(X)
temp = [arr[x] for x in X]
# print(temp)
numm = 0
for n in range(1, N+1):
    ele = str(n).zfill(K)
    ele_temp = [arr[e] for e in ele]

    cnt = 0
    for x, e in zip(temp, ele_temp):
        for i, j in zip(x,e):
            if i != j:
                cnt += 1
        if cnt > P:
            break

    if cnt <= P and cnt > 0:
        numm += 1
print(numm)