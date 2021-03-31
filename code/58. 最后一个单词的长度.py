# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/1 02:07
# Description:

__author__ = "BeiYu"


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip(" ").split(" ")[-1])
