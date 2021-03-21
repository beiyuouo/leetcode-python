# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 13:44
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies < max_candies:
                res.append(False)
            else:
                res.append(True)
        return res
