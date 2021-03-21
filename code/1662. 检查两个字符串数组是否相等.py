# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:33
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
