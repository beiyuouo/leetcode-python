# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/24 00:31
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, cnt = 0, 0
        while i < len(nums):
            if nums[i] == 0 and len(nums) - i - 1 >= cnt:
                for j in range(i, len(nums) - 1):
                    nums[j] = nums[j + 1]
                nums[-1] = 0
                cnt += 1
            else:
                i += 1
