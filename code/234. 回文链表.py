# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/27 01:39
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        q = head
        while q is not None:
            vals.append(q.val)
            q = q.next
        return vals == vals[::-1]

