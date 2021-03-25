# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/26 01:36
# Description:

__author__ = "BeiYu"

from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sumMat = []
        self.rowMax = len(matrix)
        self.colMax = len(matrix[0])

        for i in range(self.rowMax):
            sumRow = [matrix[i][0]]
            for j in range(1, self.colMax):
                sumRow.append(sumRow[-1] + matrix[i][j])
            if i > 0:
                for j in range(self.colMax):
                    sumRow[j] += self.sumMat[-1][j]
            self.sumMat.append(sumRow)

    def _sumSubMat(self, row: int, col: int) -> int:
        if row < 0 or row > self.rowMax or col < 0 or col > self.colMax:
            return 0
        return self.sumMat[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sumSubMat(row2, col2) - self._sumSubMat(row1 - 1, col2) \
               - self._sumSubMat(row2, col1 - 1) + self._sumSubMat(row1 - 1, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
if __name__ == '__main__':
    obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    # [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
    print(obj.sumRegion(2, 1, 4, 3))
    print(obj.sumRegion(1, 1, 2, 2))
    print(obj.sumRegion(1, 2, 2, 4))
