import sys
sys.stdin = open('input.txt')

# 전체 n개 , k개만 가르친다, k개로 이루어진 글자만 읽을 수 있다
N, K = map(int,input().split())
k = K-5
arr = []
for _ in range(N):
    str = input()
    str1 = ''
    for i in str:
        if i not in 'antic':
            str1 += i
    arr.append(str1)

temp =[]
for i in arr:
    for j in i:
        if j not in temp:
            temp.append(j)
# print(temp)
# print(arr)

cnt1 = []

for i in range(1<<len(temp)): # 총 경우의 수
    cnt = []
    for j in range(len(temp)):
        if i&(1<<j):
            cnt.append(temp[j])
    if len(cnt) == k:
        cnt1.append(cnt)
print(cnt1)

for i in cnt1:
    print(i)
