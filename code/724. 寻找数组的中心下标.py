# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/16 13:56
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre_sum = []
        for i in range(len(nums)):
            if i > 0:
                pre_sum.append(pre_sum[-1] + nums[i])
            else:
                pre_sum.append(nums[i])

        def get_pre_sum(x: int) -> int:
            if x < 0:
                return 0
            if x >= len(nums):
                return pre_sum[-1]
            return pre_sum[x]

        for i in range(len(nums)):
            if get_pre_sum(i - 1) == get_pre_sum(len(nums) - 1) - get_pre_sum(i):
                return i
        return -1
