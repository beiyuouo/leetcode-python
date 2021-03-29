# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/29 01:09
# Description:

__author__ = "BeiYu"


class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {')': '(', ']': '[', '}': '{'}

        class Stack:
            def __init__(self):
                self.stk = []

            def get_top(self):
                return None if len(self.stk) == 0 else self.stk[-1]

            def pop(self):
                self.stk.pop(-1)

            def push(self, _ch: str):
                self.stk.append(_ch)

            def __len__(self):
                return len(self.stk)

        stack = Stack()

        for ch in s:
            if ch not in pair_dict.keys():
                stack.push(ch)
            else:
                if stack.get_top() != pair_dict[ch]:
                    return False
                else:
                    stack.pop()
        if len(stack) > 0:
            return False
        return True