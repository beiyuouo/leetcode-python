# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/3 16:03
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        while len(nums1) > m:
            nums1.pop()

        nums1.extend(nums2)
        nums1.sort()
