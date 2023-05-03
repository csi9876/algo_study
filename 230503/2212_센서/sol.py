import sys
sys.stdin = open('input.txt')



N = int(input())
K = int(input())
# print(N, K)
arr = list(map(int, input().split()))
if N<=K:
    print(0)
else:
    arr.sort()
    # print(arr)

    temp = []
    for i in range(N-1):
        temp.append((arr[i+1]-arr[i], i, i+1))

    temp.sort(reverse=True)
    # print(temp)
    result = []
    for i in range(K-1):
        result.append((temp[i][1],temp[i][2]))

    # print(result)
    s = arr[0]
    res = 0
    e = arr[-1]
    for i in range(len(result)):
        res += arr[result[i][0]] - s
        s = arr[result[i][1]]

    res += e-s

    print(res)