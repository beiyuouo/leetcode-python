# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/19 16:44
# Description:

__author__ = "BeiYu"


class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            cnt += 1
        return cnt
