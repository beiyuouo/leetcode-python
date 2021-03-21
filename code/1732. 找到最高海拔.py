# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/19 16:55
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        cur = 0
        for x in gain:
            cur += x
            res = max(res, cur)
        return res
