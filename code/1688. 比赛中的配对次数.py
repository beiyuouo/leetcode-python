# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/21 17:06
# Description:

__author__ = "BeiYu"


class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            res += n // 2
            n = n // 2 if n % 2 == 0 else n // 2 + 1
        return res
