# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/9 11:30
# Description:

__author__ = "BeiYu"


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        res = ""
        while columnNumber > 0:
            columnNumber -= 1
            res += dic[columnNumber % 26]
            columnNumber //= 26

        return res[::-1]
