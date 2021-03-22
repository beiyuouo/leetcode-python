# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 12:25
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for l in accounts:
            if sum(l) > maxx:
                maxx = sum(l)
        return maxx
