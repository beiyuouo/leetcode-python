# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/15 14:07
# Description:

__author__ = "BeiYu"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
