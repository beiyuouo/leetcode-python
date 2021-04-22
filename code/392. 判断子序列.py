# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/23 10:35
# Description:

__author__ = "BeiYu"


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur = 0
        for i in range(len(t)):
            if cur < len(s) and s[cur] == t[i]:
                cur += 1
        return cur == len(s)
