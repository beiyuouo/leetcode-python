# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/26 01:28
# Description:

__author__ = "BeiYu"


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ss = [x for x in s]
        while l < r:
            while l < len(ss) and ss[l] not in vowels:
                l += 1
            while r >= 0 and ss[r] not in vowels:
                r -= 1
            if l < r and ss[l] in vowels and ss[r] in vowels:
                ss[l], ss[r] = ss[r], ss[l]
                l += 1
                r -= 1
        return "".join(ss)


if __name__ == '__main__':
    print(Solution().reverseVowels("leetcode"))
