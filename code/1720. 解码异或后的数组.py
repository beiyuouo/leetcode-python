# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/14 13:59
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        curr = first
        res = [curr]
        for i in encoded:
            curr = curr ^ i
            res.append(curr)
        return res
