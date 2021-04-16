# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/17 01:43
# Description:

__author__ = "BeiYu"


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def reformat(_s: str) -> str:
            itr = 0
            dic = {}
            _ss = ""
            for _ch in _s:
                if _ch not in dic.keys():
                    dic[_ch] = itr
                    itr += 1
                _ss += chr(ord("a")+dic[_ch])
            return _ss

        return reformat(s) == reformat(t)
