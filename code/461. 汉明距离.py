# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/23 01:22
# Description:

__author__ = "BeiYu"


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            if x % 2 != y % 2:
                cnt += 1
            x, y = x//2, y//2
        return cnt
