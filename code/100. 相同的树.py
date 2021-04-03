# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/3 16:12
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def _have(t):
            return t is not None

        if _have(p) != _have(q): return False
        if not _have(p): return True
        if p.val != q.val: return False

        if _have(p.left) != _have(q.left): return False
        if _have(p.right) != _have(q.right): return False

        flag = True
        if _have(p.left):
            flag = flag and self.isSameTree(p.left, q.left)

        if _have(p.right):
            flag = flag and self.isSameTree(p.right, q.right)

        return flag
