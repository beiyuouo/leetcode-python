# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/24 01:14
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        pre_sum = [arr[0]]

        for i in range(1, len(arr)):
            tmp = arr[i] + pre_sum[-1]
            pre_sum.append(tmp)

        def _get_psum(idx: int) -> int:
            if idx < 0 or idx > len(pre_sum):
                return 0
            return pre_sum[idx]

        def _get_sum(lidx: int, ridx: int) -> int:
            return _get_psum(ridx) - _get_psum(lidx - 1)
        # print(pre_sum)
        for i in range(len(arr)-2):
            if _get_sum(0, i) * 2 == _get_sum(i + 1, len(arr) - 1):
                for j in range(i+1, len(arr)-1):
                    if _get_sum(i+1, j) == _get_sum(j+1, len(arr)-1):
                        return True

                # fuck, i forget that negative numbers are exist in array, so that the prefix
                # sum doesn't have monotonicity.
                # l, r = i + 1, len(arr) - 1
                # while l <= r:
                #     mid = (l + r) // 2
                #     if _get_sum(i + 1, mid) < _get_sum(mid + 1, len(arr) - 1):
                #         l = mid + 1
                #     else:
                #         r = mid - 1
                # print(i, l, r)
                # if _get_sum(i + 1, l) == _get_sum(l + 1, len(arr) - 1):
                #     return True

        return False
