import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

s = input().strip()
t = input().strip()
res = 0
flag = 0

while t != s:
    if t == s:
        res = 1
        break

    if len(t) == 0:
        flag = 1
        break

    if t[-1] == 'A':
        t = t[:-1]
    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]
res = 1
if flag == 1:
    res = 0

print(res)

#
# S = input()
# T = input()
# S를 T로
# 뒤에 A 추가
# 뒤집고 뒤에 B 추가
# set1 = set()
# print(S, T)
# def check(s, t):
#     while s != t:
#         temp = 0
#         if s == t:
#             return 1
#         if len(s) == len(t) and s != t:
#             return 0
#         # print(s, t)
#         if s+'A' not in set1:
#             temp += 1
#             set1.add(s + 'A')
#             check(s+'A', t)
#
#         if s[::-1]+'B' not in set1:
#             temp += 1
#             set1.add(s[::-1] + 'B')
#             check(s[::-1]+'B', t)
#         if temp == 0:
#             if t == s + 'A' and t == s[::-1]+'B':
#                 print(1)
#                 exit()
#             else:
#                 return 0
#                 break
#     print(1)
#     exit()
#
# print(check(S, T))


# s = input().strip()
# t = input().strip()
# # print(a, b)
#
# res = 0
# try:
#     while t != s:
#         if t == s:
#             res = 1
#             break
#
#         if len(t) == 0:
#             pass
#
#         if t[-1] == 'A':
#             t = t[:-1]
#         elif t[-1] == 'B':
#             t = t[:-1:-1]
#
#     res = 1
#
# except:
#     res = 0
#
#
# print(res)