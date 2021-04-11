# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/12 01:16
# Description:

__author__ = "BeiYu"


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        arr1 = [x for x in s1]
        arr2 = [x for x in s2]
        arr1.sort()
        arr2.sort()
        return ''.join(arr1) == ''.join(arr2)
