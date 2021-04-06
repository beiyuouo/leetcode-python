# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/6 19:05
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1] > 0:
                res += prices[i] - prices[i - 1]

        return res
