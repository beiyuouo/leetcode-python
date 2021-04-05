# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/3 16:26
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(1, self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
