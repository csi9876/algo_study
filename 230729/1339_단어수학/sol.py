import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]
# print(arr)
dict1 = {}

for word in arr:
    temp = len(word) -1
    for i in word:
        if i in dict1:
            dict1[i] += pow(10, temp)
        else:
            dict1[i] = pow(10, temp)
        temp -= 1

dict1 = sorted(dict1.values(), reverse=True)

ans = 0
res = 9
for i in dict1:
    ans += res * i
    res -= 1

print(ans)