# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:21
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
