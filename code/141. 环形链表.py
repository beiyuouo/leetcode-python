# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/7 19:59
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        while p:
            if p.next == -1: return True
            q = p.next
            p.next = -1
            p = q
        return False
