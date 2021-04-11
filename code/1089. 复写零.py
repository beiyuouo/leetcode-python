# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/11 16:45
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        new_arr = []
        for i in range(n):
            if arr[i] == 0:
                new_arr.append(0)
            new_arr.append(arr[i])
            if len(new_arr) >= n:
                break

        arr[:] = new_arr[:n]
