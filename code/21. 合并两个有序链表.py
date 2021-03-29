# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/29 01:09
# Description:

__author__ = "BeiYu"

import math


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        rt = p = ListNode()

        def _add(x: int, _p: ListNode) -> ListNode:
            _p.next = ListNode(x)
            _p = _p.next
            return _p

        def _get_next(_l: ListNode):
            if _l:
                return _l.val
            return math.inf

        while l1 or l2:
            if _get_next(l1) < _get_next(l2):
                p = _add(_get_next(l1), p)
                l1 = l1.next
            else:
                p = _add(_get_next(l2), p)
                l2 = l2.next

        return rt.next
