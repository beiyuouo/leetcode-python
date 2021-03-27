# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/28 00:57
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        ans = ""

        for i in range(min_len, -1, -1):
            prefix = strs[0][:i + 1]
            flag = True
            for ss in strs:
                if not ss.startswith(prefix):
                    flag = False
                    break

            if flag:
                ans = prefix
                break

        return ans
