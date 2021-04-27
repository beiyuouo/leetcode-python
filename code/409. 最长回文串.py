# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/28 00:45
# Description:

__author__ = "BeiYu"


class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for ch in s:
            if ch not in dic:
                dic[ch] = 0
            dic[ch] += 1

        res = 0
        flag = False
        for ch in dic.keys():
            res += (dic[ch] // 2) * 2
            if dic[ch] % 2 == 1:
                flag = True

        return res + 1 if flag else res
