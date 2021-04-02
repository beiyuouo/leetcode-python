# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/2 15:50
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        q = head
        while q:
            while q.next and q.next.val == q.val:
                q.next = q.next.next

            q = q.next

        return head
