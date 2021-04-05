# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/4/5 17:37
# Description:

__author__ = "BeiYu"


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False

        def is_leaf(x: TreeNode):
            if x.left or x.right: return False
            return True

        global flag
        flag = False

        def dfs(x: TreeNode, tot: int):
            if is_leaf(x):
                global flag
                if tot + x.val == targetSum: flag = True
                return

            if x.left: dfs(x.left, tot + x.val)
            if x.right: dfs(x.right, tot + x.val)

        dfs(root, 0)

        return flag
