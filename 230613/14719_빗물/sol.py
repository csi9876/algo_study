import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

# N, K = map(int, input().split())
# arr = list(map(int, input().split()))
# # print(arr)
#
# set1 = set(arr)
# set2 = list(set1)
# # print(set2)
# dict1 = dict()
# for i in set2:
#     dict1[i] = 0
# # print(dict1)
# maxn = 0
#
# temp = []
#
# for i in arr:
#     dict1[i] += 1
#     temp.append(i)
#
#     if dict1[i] > K:
#         while temp:
#             numm = temp.pop(0)
#             dict1[numm] -= 1
#             if numm == i:
#                 break
#     maxn = max(maxn, len(temp))
# print(maxn)



N, K = map(int, input().split())
arr = list(map(int, input().split()))

set1 = set(arr)
set2 = list(set1)
dict1 = dict()

for i in set2:
    dict1[i] = 0

temp = []
maxn = 0

for i in arr:
    dict1[i] += 1
    temp.append(i)

    if dict1[i] > K:
        while temp:
            numm = temp.pop(0)
            dict1[numm] -= 1
            if numm == i:
                break
    maxn = max(maxn, len(temp))
print(maxn)