# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/24 00:46
# Description:

__author__ = "BeiYu"

from copy import copy
from typing import List

# TODO: O(n2logn) can not accept this problem

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []

        dic = {}
        res = []
        res_dic = {}

        def _add_pair(x: int, y: int):
            if -(x + y) not in dic.keys():
                dic[-(x + y)] = []
            if x > y: x, y = y, x

            if [x, y] not in dic[-(x + y)]:
                dic[-(x + y)].append([x, y])

        def _hash(x: List) -> int:
            return x[0]*10**10 + x[1]*10**5 + x[2]*10**0

        _add_pair(nums[0], nums[1])

        for i in range(2, len(nums)):
            if nums[i] in dic.keys():
                for j in range(len(dic[nums[i]])):
                    tmp = sorted([dic[nums[i]][j][0], dic[nums[i]][j][1], nums[i]])

                    if _hash(tmp) not in res_dic.keys():
                        res.append(tmp)
                        res_dic[_hash(tmp)] = 1

            for j in range(i):
                _add_pair(nums[j], nums[i])

        return res
