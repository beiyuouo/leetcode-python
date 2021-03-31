# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/1 01:32
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        h = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            h += 1
            nums[h] = nums[i]
        return h + 1
