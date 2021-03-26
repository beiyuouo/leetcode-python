# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/27 01:11
# Description:

__author__ = "BeiYu"

import math


class Solution:
    eps = 1e-6

    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # print(math.log(n, 4))
        _log = int(math.log(n, 4) + self.eps)
        return n == 4 ** _log
