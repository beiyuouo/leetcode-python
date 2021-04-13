# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/14 01:38
# Description:

__author__ = "BeiYu"

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ['+', '-', '*', '/']

        class Stack(object):
            def __init__(self):
                self.stack = []

            def top(self):
                return self.stack[-1]

            def pop(self):
                self.stack.pop(-1)

            def push(self, x):
                self.stack.append(x)

        stk = Stack()

        for token in tokens:
            if token in symbols:
                y = stk.top()
                stk.pop()
                x = stk.top()
                stk.pop()

                if token == '+':
                    z = x + y
                elif token == '-':
                    z = x - y
                elif token == '*':
                    z = x * y
                else:
                    z = int(x / y)
                stk.push(z)
            else:
                stk.push(int(token))

        return stk.top()
