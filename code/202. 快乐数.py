# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/25 10:04
# Description:

__author__ = "BeiYu"


class Solution:
    def isHappy(self, n: int) -> bool:
        def getsqsum(x: int) -> int:
            res = 0
            for ch in str(x):
                res += int(ch) ** 2
            return res

        dic = {}
        dic[n] = 1
        while True:
            n = getsqsum(n)
            if n == 1:
                return True
            if n in dic.keys():
                break
            dic[n] = 1
        return False
