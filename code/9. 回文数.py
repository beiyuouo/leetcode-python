# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 12:29
# Description:

__author__ = "BeiYu"


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
