# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/27 01:37
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                return nums[i]
            dic[nums[i]] = 1

