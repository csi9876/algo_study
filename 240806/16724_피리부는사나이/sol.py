import sys
sys.stdin = open('input.txt')

import sys

input = sys.stdin.readline


while True:
    m = int(input())

    if m == 0:
        break
    str = input().strip()

    dict1 = dict()
    s = e = 0
    cnt = 0

    while e < len(str):  # 문자열의 끝까지 반복
        if len(dict1) < m:  # 현재 문자가 m개 미만일 경우
            dict1[str[e]] = dict1.get(str[e], 0) + 1    # 문자의 개수 증가
            e += 1
        else:   # 현재 고유 문자가 m개일 경우
            if str[e] in dict1:     # 끝 인덱스 문자가 딕셔너리에 있을 경우
                dict1[str[e]] += 1  # 문자의 개수 증가
                e += 1
            else:
                dict1[str[s]] -= 1  # 시작 인덱스 문자의 개수 감소
                if dict1[str[s]] == 0:  # 개수가 0이면
                    del dict1[str[s]]   # 해당 문자 삭제
                s += 1

        # 현재 고유 문자의 개수 m개 이하면
        if len(dict1) <= m:
            cnt = max(cnt, e-s)

    print(cnt)