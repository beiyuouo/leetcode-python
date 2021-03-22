# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/23 01:35
# Description: 这道题让我最恶心的一点就是卡Python常数，我服了。不能每次更新答案就更新答案的字符串，只记录起始和终止位置即可

__author__ = "BeiYu"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[False for i in range(n)] for j in range(n)]

        ans = 1
        _start_idx = 0
        _end_idx = 0

        for i in range(n):
            f[i][i] = True

        for i in range(n - 1):
            f[i][i + 1] = s[i] == s[i + 1]
            if f[i][i + 1]:
                if 2 > ans:
                    ans = 2
                    _start_idx = i
                    _end_idx = i + 1

        for _len in range(3, n + 1):
            for start_idx in range(n - _len + 1):
                end_idx = start_idx + _len - 1
                f[start_idx][end_idx] = f[start_idx + 1][end_idx - 1] and s[start_idx] == s[end_idx]
                if f[start_idx][end_idx]:
                    if _len > ans:
                        ans = _len
                        _start_idx = start_idx
                        _end_idx = end_idx

        return s[_start_idx: _end_idx + 1]