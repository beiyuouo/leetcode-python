# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/17 01:39
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res = []
        itr = 1
        while True:
            if len(str(itr)) > n:
                break
            res.append(itr)
            itr += 1

        return res
