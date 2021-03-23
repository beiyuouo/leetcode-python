# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/24 00:39
# Description:

__author__ = "BeiYu"


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # f[i][j]表示前i位最后j结尾的方案数
        import numpy as np
        f = np.zeros((n, 5))
        f[0] = np.array([1, 1, 1, 1, 1])
        for i in np.arange(1, n):
            for j in np.arange(5):
                f[i][j] = f[i - 1][j]
                for k in np.arange(j):
                    f[i][j] += f[i - 1][k]

        return int(sum(f[n - 1]))
