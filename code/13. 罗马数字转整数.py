# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/28 00:45
# Description:

__author__ = "BeiYu"


class Solution:
    def romanToInt(self, s: str) -> int:
        word_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        cur = 0

        def _getnextchar(idx: int):
            if idx + 1 >= len(s):
                return None
            return s[idx + 1]

        for i in range(len(s)):
            if (s[i] == 'I' and (_getnextchar(i) == 'V' or _getnextchar(i) == 'X')) \
                    or (s[i] == 'X' and (_getnextchar(i) == 'L' or _getnextchar(i) == 'C')) \
                    or (s[i] == 'C' and (_getnextchar(i) == 'D' or _getnextchar(i) == 'M')):
                cur -= word_to_int[s[i]]
            else:
                cur += word_to_int[s[i]]

        return cur
