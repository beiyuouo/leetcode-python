# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/28 01:02
# Description:

__author__ = "BeiYu"

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while 2 * (a ** 2) <= c:
            b = int(math.sqrt(c - a ** 2))
            if a * a + b * b == c:
                return True
            a = a + 1
        return False
