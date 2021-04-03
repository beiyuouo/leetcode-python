# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/3 16:19
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _have(t):
            return t is not None

        def isSymmetry(p: TreeNode, q: TreeNode) -> bool:
            if _have(p) != _have(q): return False
            if not _have(p): return True
            if p.val != q.val: return False

            if _have(p.left) != _have(q.right): return False
            if _have(p.right) != _have(q.left): return False

            flag = True
            if _have(p.left):
                flag = flag and isSymmetry(p.left, q.right)

            if _have(p.right):
                flag = flag and isSymmetry(p.right, q.left)

            return flag

        if not _have(root): return True
        if _have(root.left) != _have(root.right): return False
        if _have(root.left): return isSymmetry(root.left, root.right)
        return True
