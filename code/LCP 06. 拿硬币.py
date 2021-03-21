# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/15 14:12
# Description:

__author__ = "BeiYu"

from typing import List
import math


class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for coin in coins:
            res += math.ceil(coin / 2)
        return res
