# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/24 01:37
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        global res
        res = 0

        def is_child(x: TreeNode):
            return x is not None and x.left is None and x.right is None

        def dfs(x: TreeNode):
            if x is None: return
            if x.left: dfs(x.left)
            if x.right: dfs(x.right)
            global res
            if is_child(x.left): res += x.left.val

        dfs(root)

        return res
