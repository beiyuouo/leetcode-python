# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/17 14:33
# Description:

__author__ = "BeiYu"


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cur = 0
        for _s in s:
            if _s == '(':
                cur += 1
            elif _s == ')':
                cur -= 1
            res = max(res, cur)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxDepth("(1+(2*3)+((8)/4))+1"))
