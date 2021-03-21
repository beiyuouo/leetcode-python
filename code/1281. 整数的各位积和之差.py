# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:20
# Description:

__author__ = "BeiYu"


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def _calc_sum(s: str):
            res = 0
            for ch in s:
                res += int(ch)
            return res

        def _calc_mul(s: str):
            res = 1
            for ch in s:
                res *= int(ch)
            return res

        return _calc_mul(str(n)) - _calc_sum(str(n))
