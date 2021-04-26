# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/27 01:34
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        for i in range(n):
            A[m + i] = B[i]

        sorted(A)
