# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/27 00:59
# Description:

__author__ = "BeiYu"

from queue import LifoQueue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = LifoQueue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        n = self.q.qsize()
        self.q.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.get()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q.empty()
