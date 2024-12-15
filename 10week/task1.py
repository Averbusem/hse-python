"""
https://leetcode.com/problem-list/binary-tree/?difficulty=MEDIUM
URL: https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_sum):
            if not node:
                return 0

            cur_sum = cur_sum * 10 + node.val

            if not node.left and not node.right:
                return cur_sum

            left_sum = dfs(node.left, cur_sum)
            right_sum = dfs(node.right, cur_sum)

            return left_sum + right_sum

        return dfs(root, 0)
