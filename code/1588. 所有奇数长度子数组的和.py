# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/21 17:07
# Description:

__author__ = "BeiYu"

from typing import List
import math


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            res += arr[i] * ((i//2 + 1) * ((len(arr) - i - 1) // 2 + 1)
                             + math.ceil(i / 2) * math.ceil((len(arr) - i - 1) / 2))
            # print(i, (i//2 + 1) * ((len(arr) - i - 1) // 2 + 1),
            #       math.ceil(i / 2) * math.ceil((len(arr) - i - 1) / 2))
        return res


if __name__ == '__main__':
    print(Solution().sumOddLengthSubarrays([1, 4, 2, 5, 3]))
