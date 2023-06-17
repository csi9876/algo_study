import sys
sys.stdin = open('input.txt')

h, w = map(int, input().split())
arr = list(map(int, input().split()))
temp = 0

for i in range(1, w-1):
    s = max(arr[:i])
    e = max(arr[i+1:])
    minn = min(s,e)

    if minn > arr[i]:
        temp += minn - arr[i]
print(temp)