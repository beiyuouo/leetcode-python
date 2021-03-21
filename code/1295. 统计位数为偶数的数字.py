# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/19 16:44
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                cnt += 1
        return cnt
