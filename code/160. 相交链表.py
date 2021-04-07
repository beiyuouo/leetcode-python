# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/8 02:10
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        q = headA
        map = {}
        while q:
            map[q] = 1
            q = q.next

        q = headB
        while q:
            if q in map.keys():
                return q
            q = q.next

        return None
