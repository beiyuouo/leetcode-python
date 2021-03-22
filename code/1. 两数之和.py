# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 12:29
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums[i + 1:]):
                if n1 + n2 == target:
                    return [i, j + i + 1]
