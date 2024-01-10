import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	n = int(input())
	arr = [list(map(int, input().strip())) for _ in range(n)]
	arr.sort()
	ans = True
	# 초기값 가장 짧은 번호
	min_n = arr[0]

	# 초기값 제외 모든 번호 순회
	for i in range(len(arr) - 1):
		# 길이 저장
		temp = len(arr[i])
		# 현재 번호와 다음 번호의 현재 길이만큼이 같으면
		# 일관성 X
		if arr[i+1][:temp] == arr[i]:
			ans = False

	if ans:
		print("YES")
	else:
		print("NO")