import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

S = int(input())
v = [[0] * (S + 1) for i in range(S + 1)]
num = 1
clip = 0
que = deque([(num, clip)])
minn = 1001

while que:
    nn, cc = que.popleft()
    if nn == S:
        minn = min(minn, v[nn][cc] - 1)

    dx = [cc, 0, -1]
    for i in range(3):
        nx = nn + dx[i]
        if 0<= nx <= S:
            if v[nx][nn] == 0 and i == 1:
                v[nx][nn] = v[nn][cc] + 1
                que.append((nx, nn))

            if v[nx][cc] == 0 and i != 1:
                v[nx][cc] = v[nn][cc] + 1
                que.append((nx, cc))

print(minn)

# S = int(input())
# v = [[-1]*(S+1) for _ in range(S+1)]
# num = 1
# cc = 0
# v[1][0]=0
# minn = 1000
# que = deque([(num, cc)])
# # print(que)
# minn = 1001
# while que:
#     nn, cc = que.popleft()  # x는 화면 갯수 , c는 클립보드 갯수
#     if nn == S:
#         print(v[nn][cc])
#         break
#         # minn = min(minn, v[nn][cc])
#
#     temp = [nn+cc, nn, nn-1]  # 현재 화면 갯수+클립보드 수, 클립보드에 저장, 화면 갯수 -1
#     for nx in temp:
#         if nx < 0 or nx > num:
#             continue
#         # 클립보드에 저장하는 경우의 다음 캐쉬 위치 수정 및 다음 큐에 들어가는 데이터 수정
#         # 클립보드에 저장하는 경우에는 방문 체크를 다르게 해줘야함.
#         if v[nx][nn] == -1 and nx == nn:
#             # dx가 0, 클립보드에 저장하는 경우
#             # temp=c
#             # c=x    클립보드에 현재 화면 갯수 입력
#             # s[nx][c]=s[x][temp]+1
#             # q.append((nx,c))
#             v[nx][nn] = v[nn][cc] + 1
#             que.append((nx, nn))
#
#         if v[nx][cc] == -1 and nx != nn:
#             v[nx][cc] = v[nn][cc] + 1
#             que.append((nx, cc))

# while que:
#     num, cc = que.popleft()
#     if num == S:
#         minn = min(minn, v[num][cc])
#
#     temp = [num + cc, num, num-1]
#     for i in temp:
#         if 0 <= i <= S and v[i][num] == 0 and i == num:
#             v[i][num] = v[num][cc] + 1
#             que.append((i, num))
#
#         if v[i][cc] == 0 and i != num:
#             v[i][cc] = v[num][cc] + 1
#             que.append((i, cc))



'''
1 >> 2
1 >> 2 >> 4
1 >> 2 >> 4 > 6
1 >> 2 > 3 >> 6 > 9 >> 18

'''