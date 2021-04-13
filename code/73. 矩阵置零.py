# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/13 20:42
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ban_row = {}
        ban_col = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    ban_row[i] = 1
                    ban_col[j] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in ban_row.keys() or j in ban_col.keys():
                    matrix[i][j] = 0
