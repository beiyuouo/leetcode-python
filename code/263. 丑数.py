# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/16 13:47
# Description:

__author__ = "BeiYu"

import math


class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0 or n == 1 or n == -1:
            return False

        while n % 2 == 0:
            n //= 2

        while n % 3 == 0:
            n //= 3

        while n % 5 == 0:
            n //= 5

        if n == 1:
            return True
        else:
            return False
