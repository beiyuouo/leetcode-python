# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/1 02:07
# Description:

__author__ = "BeiYu"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
