import sys
sys.stdin = open('input.txt')

# import sys
# input = sys.stdin.readline

from collections import deque

X = int(input())
arr = list(input())
n = len(arr)
pattern = [arr[:]]      # 주기 저장

while 1:
    frr = deque(arr[:n//2+1])   # 앞 절반
    brr = deque(arr[n//2+1:])   # 뒷 절반
    arr = []
    for _ in range(len(brr)):
        arr.append(frr.popleft())
        arr.append(brr.pop())
    arr += frr
    # 패턴의 첫 요소(원본 문자열)과 같다면 종료
    if arr == pattern[0]:
        break
    # 패턴에 arr 추가
    pattern.append(arr[:])

# 패턴의 첫 요소와 나머지 요소의 역순 배열
pattern = [pattern[0]] + pattern[1:][::-1]

# x번째 정렬 패턴 출력
print("".join(pattern[X % len(pattern)]))