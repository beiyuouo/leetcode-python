# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/27 01:16
# Description:

__author__ = "BeiYu"


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        f = [0 for i in range(11)]
        f[0], f[1] = 0, 10

        def _P(_n: int) -> int:
            _res = 1
            for _i in range(1, _n + 1):
                _res *= _i
            return _res

        def _A(_n: int, _m: int) -> int:
            return _P(_n) // _P(_n - _m)

        def _C(_n: int, _m: int) -> int:
            return _P(_n) // _P(_n - _m) // _P(_m)

        for i in range(2, 11):
            f[i] = 9 * _A(9, i - 1)

        res = 0
        for i in range(min(n + 1, 11)):
            res += f[i]
        # print(f)
        return res


if __name__ == '__main__':
    print(Solution().countNumbersWithUniqueDigits(2))
