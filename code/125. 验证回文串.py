# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/7 19:07
# Description:

__author__ = "BeiYu"


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]
