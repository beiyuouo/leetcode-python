# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/28 00:54
# Description:

__author__ = "BeiYu"


class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        for i in range(n):
            f.append((f[-1] + f[-2]) % 1000000007)

        return f[n]
