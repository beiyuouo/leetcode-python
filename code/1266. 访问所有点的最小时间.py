# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/19 16:36
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def _get_time(p1: List[int], p2: List[int]):
            dx, dy = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
            return max(dx, dy)

        res = 0
        for i in range(len(points) - 1):
            res += _get_time(points[i], points[i + 1])
        return res
