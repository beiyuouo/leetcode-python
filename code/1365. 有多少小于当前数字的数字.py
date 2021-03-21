# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:33
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        def _calc(x: int) -> int:
            cnt = 0
            for i in nums:
                if i < x:
                    cnt += 1
            return cnt

        res = []
        for num in nums:
            res.append(_calc(num))

        return res
