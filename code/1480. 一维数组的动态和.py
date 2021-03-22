from typing import *


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        tot = 0
        for i in nums:
            tot += i
            res.append(tot)
        return res
