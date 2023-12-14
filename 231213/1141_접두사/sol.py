import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr.sort(key=len)       # 길이 순 정렬
cnt = 0     # 카운트 변수

for i in range(n):
    temp = False        # 부분 문자열 일치 여부 확인
    for j in range(i+1, n):     # 현재 원소 다음부터 조회
        if arr[i] == arr[j][0:len(arr[i])]:     # 부분 문자열인지 확인
            temp = True     # 일치하면 true로 설정
            break   #   종료
    if not temp:    # 부분 문자열이 아니면
        cnt += 1    # 카운트 증가
print(cnt)  # 출력