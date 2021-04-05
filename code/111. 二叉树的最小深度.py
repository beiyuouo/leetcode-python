# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/5 17:25
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0

        def _have(x):
            return x is not None

        if _have(root.left) and _have(root.right):
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

        if _have(root.left): return self.minDepth(root.left)

        if _have(root.right): return self.minDepth(root.right)

        return 1
