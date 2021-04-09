# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/9 11:31
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = nums[0]
                    count = 1
        return num
