from heapq import heappush, heappop



def abc(start):
    que = []
    heappush(que,start)

    while que:
        cost, now = heappop(que)
        if v[now] < cost:
            continue
        for i in arr[now]:
            res = cost + i[0]
            if res < v[i[1]]:
                v[i[1]] = res
                heappush(que,(res,i[1]))
                print(v)




n = int(input())
m = int(input())
arr = [[]*n]
print(arr)
비용 도착점

s, e = map(int, input().split())

arr = [[]for i in range(n+1)]
v = [int(1e9)]*(n+1)


abc(0, s)