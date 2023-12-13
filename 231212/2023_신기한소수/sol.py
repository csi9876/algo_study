import sys
sys.stdin = open('input.txt')


import sys
input = sys.stdin.readline

n = int(input())

# 소수 판별
def is_prime(x):
    # 0과 1은 소수 아님
    if x < 2:
        return False
    # 제곱근까지 확인하여 나누어 떨어지면 소수 아님
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

# 백트래킹을 활용한 신기한 소수 찾기
def find_interesting_primes(num):
    # 소수가 아니라면 진행 X
    if num > 0 and not is_prime(num):
        return
    # 신기한 소수면 출력
    if len(str(num)) == n:
        print(num)
        return
    # 자릿수를 순회하며 소수 찾기
    for i in range(10):
        # 현재 수에 10 곱하고 i 더한 수를 사용
        find_interesting_primes(num*10 + i)

# 1부터 9까지 각 자릿수에 대해 신기한 소수 찾기
for i in range(1, 10):
    find_interesting_primes(i)