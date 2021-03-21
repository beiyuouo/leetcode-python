# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/14 13:52
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        _nums = []
        for i in range(n):
            _nums.append(nums[i])
            _nums.append(nums[i + n])
        return _nums
