# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/1 01:37
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        h = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[h] = nums[i]
            h += 1
        return h
