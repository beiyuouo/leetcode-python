# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 13:40
# Description:

__author__ = "BeiYu"


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        for Ji in jewels:
            for Si in stones:
                if Ji == Si:
                    cnt += 1
        return cnt
