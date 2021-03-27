# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/28 00:26
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = None
        rt = None
        cur = 0
        flag = False

        def _addnode(_res, x: int):
            new_node = ListNode(val=x)
            print(x)
            if _res:
                _res.next = new_node
            _res = new_node
            return _res

        while l1 or l2:
            if l1:
                cur += l1.val
            if l2:
                cur += l2.val

            if not res:
                flag = True
            res = _addnode(res, cur % 10)

            if flag:
                flag = False
                rt = res

            cur //= 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        while cur > 0:
            res = _addnode(res, cur % 10)
            cur //= 10

        print(rt.val)
        return rt
