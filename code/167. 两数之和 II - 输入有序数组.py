# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/8 02:12
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            if numbers[i] in map.keys():
                return [map[numbers[i]] + 1, i + 1]
            map[target - numbers[i]] = i

        return None
