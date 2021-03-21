# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/3/15 14:06
# Description:

__author__ = "BeiYu"


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

