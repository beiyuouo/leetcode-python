# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/6 18:55
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxOut = prices[-1]
        res = 0
        for i in range(len(prices) - 1, -1, -1):
            res = max(res, maxOut - prices[i])
            maxOut = max(maxOut, prices[i])

        return res
