# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/31 01:44
# Description:

__author__ = "BeiYu"


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        desc_str = self.countAndSay(n - 1)
        desc = ""

        i, j = 0, 0
        while i < len(desc_str):
            j = i + 1
            while j < len(desc_str) and desc_str[i] == desc_str[j]:
                j += 1
            desc += str(j - i) + desc_str[i]
            i = j

        return desc
