# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/24 00:47
# Description:

__author__ = "BeiYu"


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s) // 2
        s1, s2 = s[:n], s[n:]
        cnt = 0

        def _is_vowel(ch: str):
            return ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(n):
            if _is_vowel(s1[i]):
                cnt += 1
            if _is_vowel(s2[i]):
                cnt -= 1
        return cnt == 0
