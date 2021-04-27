# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/28 00:49
# Description:

__author__ = "BeiYu"


class Solution:
    def isUnique(self, astr: str) -> bool:
        import numpy as np
        return np.unique(list(astr)).shape[0] == len(astr)
