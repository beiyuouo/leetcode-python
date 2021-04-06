# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/6 18:50
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        p = [1]
        for i in range(1, rowIndex + 1):
            p.append(p[-1] * i)

        def C(n, m):
            return p[n] // p[m] // p[n - m]

        res = []
        for i in range(rowIndex + 1):
            res.append(C(rowIndex, i))

        return res
