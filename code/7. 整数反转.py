# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 12:29
# Description:

__author__ = "BeiYu"


class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            ans = int(str(x)[::-1])
        else:
            ans = int('-' + str(abs(x))[::-1])

        if x > 2 ** 31 - 1 or x < -2 ** 31 or ans > 2 ** 31 - 1 or ans < -2 ** 31:
            return 0
        else:
            return ans
