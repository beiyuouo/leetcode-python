# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/4 16:40
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.dep = {}
        self.dep[None] = 0

    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        self.dep[root] = max(0, self.dep[root.left], self.dep[root.right]) + 1

        # print(f'{root.val} -> {self.dep[root]}, {self.dep[root.left]}, {self.dep[root.right]}')

        if abs(self.dep[root.left] - self.dep[root.right]) > 1:
            return False

        return True
