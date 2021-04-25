# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/25 09:48
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        import numpy as np
        return np.unique(nums).shape[0] != len(nums)
