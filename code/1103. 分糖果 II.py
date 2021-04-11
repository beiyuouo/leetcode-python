# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/11 16:03
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        _one = (1 + num_people) * num_people // 2

        import math

        l, r = 0, candies

        def _calc_can(x: int) -> int:
            return (1 + num_people * x) * num_people * x // 2

        while l <= r:
            mid = (l + r) // 2
            if _calc_can(mid) <= candies:
                l = mid + 1
            else:
                r = mid - 1

        res = [(i + 1) * r + num_people * (0 + r - 1) * r // 2 for i in range(num_people)]
        candies -= sum(res)

        _now = num_people * r + 1
        idx = 0
        while candies > 0:
            res[idx] += min(candies, _now)
            candies -= min(candies, _now)
            _now += 1
            idx += 1

        return res
