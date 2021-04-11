# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/12 01:10
# Description:

__author__ = "BeiYu"


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vec1 = version1.split('.')
        vec2 = version2.split('.')

        i1, i2 = 0, 0
        while i1 < len(vec1) or i2 < len(vec2):
            if i1 >= len(vec1):
                vec1.append('0')
            if i2 >= len(vec2):
                vec2.append('0')
            if int(vec1[i1]) > int(vec2[i2]):
                return 1
            elif int(vec1[i1]) < int(vec2[i2]):
                return -1
            i1 += 1
            i2 += 1

        return 0
