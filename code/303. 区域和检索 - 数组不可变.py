# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/27 00:05
# Description:

__author__ = "BeiYu"

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.arrSum = []
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            self.arrSum.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        def _getsum(x: int) -> int:
            return self.arrSum[x] if x >= 0 else 0

        return _getsum(right) - _getsum(left - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
