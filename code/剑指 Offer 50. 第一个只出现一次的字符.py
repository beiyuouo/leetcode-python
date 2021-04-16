# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/16 13:39
# Description:

__author__ = "BeiYu"


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for ch in s:
            if ch not in dic.keys():
                dic[ch] = 0
            dic[ch] += 1

        for ch in s:
            if dic[ch] == 1:
                return ch
        return " "
