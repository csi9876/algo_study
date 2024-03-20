import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = sys.maxsize

for i in range(n-3):    # i 다음 3개의 인덱스는 존재하도록
    for j in range(i+3, n): # j 전에 3개의 인덱스는 존재하도록
        # 안나 눈사람
        snow1 = arr[i] + arr[j]

        # 엘사 눈사람 포인터
        s = i + 1
        e = j - 1

        while True:
            if s == e:
                break

            # 엘사 눈사람
            snow2 = arr[s] + arr[e]
            # 차이
            temp = snow1 - snow2

            # 양수이면 엘사의 눈사람이 커지게
            if temp > 0:
                s += 1

            # 음수이면 엘사의 눈사람이 작아지게
            elif temp < 0:
                e -= 1

            # 같으면 0출력후 실행 종료
            elif temp == 0:
                print(0)
                exit()

            temp = abs(temp)

            res = min(res, temp)

print(res)