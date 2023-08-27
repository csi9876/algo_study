import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

arr = input().rstrip()
target = input().rstrip()

temp = 0
index = 0

while True:
    if index + len(target) > len(arr):
        break

    for i in range(len(target)):
        if arr[index+i] != target[i]:
            index += 1
            break
    else:
        temp += 1
        index += len(target)

print(temp)