# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:21
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i + 1] for x in range(nums[i])])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.decompressRLElist([1, 2, 3, 4]))
