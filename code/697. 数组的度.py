# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/13 20:41
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}

        for idx, num in enumerate(nums):
            if num not in count.keys():
                count[num] = []
            count[num].append(idx)

        degree = 0
        res = len(nums)
        for key in count.keys():
            if len(count[key]) > degree:
                degree = len(count[key])
                res = count[key][-1] - count[key][0] + 1
            elif len(count[key]) == degree:
                res = min(res, count[key][-1] - count[key][0] + 1)

        return res
