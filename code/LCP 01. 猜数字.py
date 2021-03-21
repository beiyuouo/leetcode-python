# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/14 13:54
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        result = [1 if guess[i] == answer[i] else 0 for i in range(len(guess))]
        return sum(result)
