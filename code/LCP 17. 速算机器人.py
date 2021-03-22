# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/23 01:20
# Description:

__author__ = "BeiYu"


class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for ch in s:
            if ch == 'A':
                x = 2 * x + y
            else:
                y = 2 * y + x
        return x + y
