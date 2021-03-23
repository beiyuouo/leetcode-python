# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/24 00:47
# Description:

__author__ = "BeiYu"


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        h1, h2 = 0, 0
        new_str: str = ""
        while h1 < len(word1) or h2 < len(word2):
            if h1 < len(word1):
                new_str += word1[h1]
            if h2 < len(word2):
                new_str += word2[h2]

            h1 += 1
            h2 += 1
        return new_str
