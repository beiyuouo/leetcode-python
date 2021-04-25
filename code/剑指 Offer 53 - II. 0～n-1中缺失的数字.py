# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/25 09:50
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_arr, xor_all = 0, 0
        for i in range(len(nums)):
            xor_arr = xor_arr ^ nums[i]
        for i in range(len(nums) + 1):
            xor_all = xor_all ^ i
        return xor_all ^ xor_arr
