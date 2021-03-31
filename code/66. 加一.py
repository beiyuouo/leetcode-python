# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/1 02:07
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(ch) for ch in str(int("".join([str(x) for x in digits])) + 1)]
