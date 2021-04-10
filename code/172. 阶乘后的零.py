# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/10 14:11
# Description:

__author__ = "BeiYu"


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        pwer = 5
        while n >= pwer:
            count += n // pwer
            pwer *= 5
        return count
