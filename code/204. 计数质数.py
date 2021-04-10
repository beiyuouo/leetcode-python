# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/10 15:43
# Description:

__author__ = "BeiYu"


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [1 for i in range(min(5, n))]
        is_prime[0] = is_prime[1] = 0
        prime = []
        for i in range(2, n):
            if is_prime[i]:
                prime.append(i)
                j = i * i
                while j < n:
                    is_prime[j] = 0
                    j += i
        return len(prime)
