# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/25 10:16
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0 for i in range(len(nums))]
        f[0] = 1
        for i in range(1, len(nums)):
            f[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
