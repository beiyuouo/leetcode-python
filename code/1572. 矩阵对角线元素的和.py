# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/19 16:56
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum([mat[x][x] for x in range(len(mat))]) + sum([mat[x][len(mat) - 1 - x] for x in range(len(mat))]) \
               - (0 if len(mat) % 2 == 0 else mat[len(mat) // 2 + 1][len(mat) // 2 + 1])
