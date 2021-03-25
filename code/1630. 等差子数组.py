# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/25 11:56
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def _check(arr: List[int]) -> bool:
            arr.sort()
            _arithmet = arr[1] - arr[0]
            for i in range(2, len(arr)):
                if arr[i] - arr[i - 1] != _arithmet:
                    return False
            return True

        res = []
        for i in range(len(l)):
            if _check(nums[l[i]: r[i] + 1]):
                res.append(True)
            else:
                res.append(False)

        return res
