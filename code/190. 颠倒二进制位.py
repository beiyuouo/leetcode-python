# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/10 15:38
# Description:

__author__ = "BeiYu"


class Solution:
    def reverseBits(self, n: int) -> int:
        _32bit = ['0' for i in range(32)]
        _32bit[-len(bin(n)[2:])] = bin(n)[2:]
        return int(''.join(_32bit[::-1]), 2)
