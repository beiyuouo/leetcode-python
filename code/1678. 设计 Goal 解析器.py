# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/16 14:13
# Description:

__author__ = "BeiYu"


class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
