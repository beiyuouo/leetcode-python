# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/15 00:59
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                if nums[i] == nums[nums[i] - 1] or nums[i] < 0 or nums[i] > N:
                    break

                t = nums[i]
                nums[i] = nums[t - 1]
                nums[t - 1] = t

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return -1
