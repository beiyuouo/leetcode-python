# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/15 00:55
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while i + 1 != nums[i]:
                if nums[nums[i] - 1] == nums[i]:
                    break
                t = nums[i]
                nums[i] = nums[t - 1]
                nums[t - 1] = t
                # print(nums)

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                res.append(nums[i])

        return res
