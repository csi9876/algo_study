import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
nums = [0] * 10

def two_point():
    l, r, cnt, kind, max_n = 0, 0, 0, 0, 0
    while r < n:
        if nums[arr[r]] == 0:
            kind += 1

        cnt += 1
        nums[arr[r]] += 1

        while kind > 2:
            nums[arr[l]] -= 1
            if nums[arr[l]] == 0:
                kind -= 1
            cnt -= 1
            l += 1

        max_n = max(max_n, cnt)
        r += 1
    return max_n

print(two_point())
