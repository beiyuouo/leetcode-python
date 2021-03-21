# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/16 14:13
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def _check(_str: str):
            for char in _str:
                if char not in allowed:
                    return False
            return True

        cnt = 0
        for word in words:
            if _check(word):
                cnt += 1

        return cnt
