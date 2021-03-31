# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/31 01:44
# Description:

__author__ = "BeiYu"

from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = 0
        min_prefix_sum = 0
        ans_sum = - math.inf
        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans_sum = max(ans_sum, prefix_sum - min_prefix_sum)
            if prefix_sum < min_prefix_sum:
                min_prefix_sum = prefix_sum

        return ans_sum
