# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/11 15:56
# Description:

__author__ = "BeiYu"


class Foo:
    def __init__(self):
        self.ok_first = False
        self.ok_second = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.ok_first = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        while not self.ok_first: pass
        printSecond()
        self.ok_second = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        while not self.ok_first or not self.ok_second: pass
        printThird()
