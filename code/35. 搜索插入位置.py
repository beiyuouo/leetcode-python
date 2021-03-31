# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/31 01:44
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return len(nums)
