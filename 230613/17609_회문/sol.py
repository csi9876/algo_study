import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

# 회문 : 앞뒤 돌려서 같은 문자
# 유사회문 : 한 글자를 삭제하면 회문

T = int(input())
arr = [2]*T
# print(arr)
for tc in range(T):
    str1 = input().strip()
    # print(str1)
    # print(str1[::-1])
    if str1 == str1[::-1]:
        arr[tc] = 0

    else:
        s = 0
        e = len(str1)-1
        flag = 0
        while flag==0:
            if str1[s] == str1[e]:
                s += 1
                e -= 1
            else:
                if s < e - 1:
                    temp = str1[:e] + str1[e + 1:]
                    print(temp)
                    if temp == temp[::-1]:
                        # print(123)
                        arr[tc] = 1
                        flag=2

                if s + 1 < e:
                    temp = str1[:s] + str1[s + 1:]
                    print(temp)
                    if temp == temp[::-1]:
                        # print(123)
                        arr[tc] = 1
                        flag=2
            if flag==0:
                break

for i in arr:
    print(i)


# T = int(input())
# arr = [2]*T
# # print(arr)
# for tc in range(T):
#     str1 = input().strip()
#     # print(str1)
#     # print(str1)
#     # print(str1[::-1])
#     if str1 == str1[::-1]:
#         arr[tc] = 0
#     else:
#         for i in range(len(str1)):
#             str2 = str1[0:i]+str1[i+1:]
#             if str2 == str2[::-1]:
#                 # print(str2)
#                 arr[tc] = 1
#                 break
#
# for i in arr:
#     print(i)