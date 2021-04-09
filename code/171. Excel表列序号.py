# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/9 11:31
# Description:

__author__ = "BeiYu"


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        map = {}
        for i in range(len(dic)):
            map[dic[i]] = i + 1

        res = 0
        columnTitle = columnTitle[::-1]
        while len(columnTitle) > 0:
            res += map[columnTitle[-1]]
            res *= 26
            columnTitle = columnTitle[:-1]

        return res
