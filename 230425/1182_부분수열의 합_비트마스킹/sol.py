import sys
sys.stdin = open('input.txt')


# N, S = map(int,input().split())
# arr = list(map(int,input().split()))
#
# count = 0
# for i in range(1<<N): # 총 경우의 수
#     temp = []
#     for j in range(N):
#         if i&(1<<j):
#             temp.append(arr[j])
#
#     if len(temp) >= 1 and sum(temp) == S:
#         # print(temp)
#         count += 1
# print(count)



N, S = map(int,input().split())
arr = list(map(int,input().split()))

count = 0
for i in range(1, 1<<N): # 총 경우의 수
    temp = 0
    for j in range(N):
        if i&(1<<j):
            temp += (arr[j])

    if temp == S:
        count += 1
print(count)