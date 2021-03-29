# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/29 01:00
# Description:

__author__ = "BeiYu"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        head = 0
        res = 0
        last_letter = {}

        def _last(_ch: str) -> int:
            if _ch not in last_letter.keys():
                return -1
            return last_letter[_ch]

        def _update(_ch: str, _idx: int) -> None:
            last_letter[_ch] = _idx

        for i in range(len(s)):
            if _last(s[i]) != -1:
                head = max(head, _last(s[i])+1)
            res = max(res, i - head + 1)
            _update(s[i], i)

        return res
