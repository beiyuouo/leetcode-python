# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 13:31
# Description:

__author__ = "BeiYu"


class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
        s = str(n)
        cnt = 0
        for i in range(len(s)):
            if s[i] == '1':
                cnt += 1
                # print(i)

        return cnt
