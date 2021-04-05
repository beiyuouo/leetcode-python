# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/5 17:39
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        res.append([1])
        for i in range(1, numRows):
            new_row = [1]
            for j in range(i - 1):
                new_row.append(res[-1][j] + res[-1][j + 1])
            new_row.append(1)
            res.append(new_row)

        return res
