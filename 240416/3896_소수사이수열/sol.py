import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline

from bisect import bisect

max_n = 1299710
is_prime = [True] * max_n
primes = []
for i in range(2, max_n):
    if is_prime[i]:
        primes.append(i)
        # # i의 배수를 모두 소수가 아닌 것으로 표시
        for j in range(i ** 2, max_n, i):
            is_prime[j] = False

for _ in range(int(input())):
    k = int(input())

    # 소수인 경우
    if is_prime[k]:
        print(0)

    else:    # 소수 아닌 경우, k보다 큰 가장 가까운 소수의 인덱스를 찾음
        idx = bisect(primes, k)
        print(primes[idx] - primes[idx - 1])