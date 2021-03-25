# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/25 11:51
# Description:

__author__ = "BeiYu"

import math


class Solution:
    eps = 1e-6

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        print(math.log(n, 3))
        _log = int(math.log(n, 3) + self.eps)
        return n == 3 ** _log


if __name__ == '__main__':
    print(Solution().isPowerOfThree(243))
