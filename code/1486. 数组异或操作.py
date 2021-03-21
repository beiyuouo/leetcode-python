# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/14 13:56
# Description:

__author__ = "BeiYu"


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res = res ^ (start + 2 * i)
        return res
