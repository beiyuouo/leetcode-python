# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/2 15:47
# Description:

__author__ = "BeiYu"


class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        eps = 1e-6
        return int(math.floor(math.sqrt(x) + eps))
