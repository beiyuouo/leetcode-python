# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/17 01:41
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        _matrix = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                _matrix[i][j] = matrix[j][i]

        return _matrix
