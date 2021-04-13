# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/14 01:34
# Description:

__author__ = "BeiYu"

from typing import List, Dict


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def get_dic(strs: str) -> Dict:
            dic = {}
            for chs in strs:
                if chs not in dic.keys():
                    dic[chs] = 0
                dic[chs] += 1
            return dic

        chars_dic = get_dic(chars)
        res = 0
        for word in words:
            word_dic = get_dic(word)

            def check(_char_dic: Dict, _word_dic: Dict) -> bool:
                for key in _word_dic:
                    if key not in _char_dic or _char_dic[key] < _word_dic[key]:
                        return False

                return True

            if check(chars_dic, word_dic):
                res += len(word)

        return res
