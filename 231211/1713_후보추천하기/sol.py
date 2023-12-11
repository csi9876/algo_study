import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
students = list(map(int, input().split()))
picture = [] # 사진틀
score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트

for i in range(m):
    if students[i] in picture:  # 사진틀에 이미 있으면
        for j in range(len(picture)):
            if students[i] == picture[j]:
                score[j] += 1   # 점수증가
    else:   # 사진틀에 없고
        if len(picture) >= n:   # 사진틀 꽉차있으면
            for j in range(n):
                if score[j] == min(score):   # 가장 적은 점수 찾기, 삭제
                    del picture[j]
                    del score[j]
                    break    # 찾으면 스탑
        picture.append(students[i])  # 새로운 녀석을 더하기
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))