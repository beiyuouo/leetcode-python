# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/22 13:48
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        str2idx = {"type": 0, "color": 1, "name": 2}
        ruleKey = str2idx[ruleKey]
        cnt = 0
        for item in items:
            if item[ruleKey] == ruleValue:
                cnt += 1
        return cnt
