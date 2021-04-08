# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/7 19:52
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]
