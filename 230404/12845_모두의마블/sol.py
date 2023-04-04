import sys
sys.stdin = open('input.txt')

n = int(input())
# 두 카드는 인접
# 업그레이드 카드 레벨은 변하지 않는다
arr = list(map(int, input().split()))
print(arr)
lv = 0
count = 0
arr.sort(reverse=True)
print(arr)
for i in range(n):
    if lv == 0:
        lv = arr[i]
    else:
        count += lv+arr[i]
        lv = min(lv, arr[i])

print(count)