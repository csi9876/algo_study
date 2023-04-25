import sys
sys.stdin = open('input.txt')

# N 문제 갯수 / L<= 난이도 합 <= R /
# 가장 어려운 문제와 쉬운 문제 난이도 차이가 >= X

N, L, R, X = map(int,input().split())
arr = list(map(int,input().split()))

count = 0
result = []
for i in range(1<<N): # 총 경우의 수
    temp = []
    for j in range(N):
        if i&(1<<j):
            temp.append(arr[j])

    # print(temp, i)
    if len(temp) > 1 and L<= sum(temp) <= R and max(temp)-min(temp) >= X:
        result.append(temp)
# print(temp)
# print(result)
print(len(result))