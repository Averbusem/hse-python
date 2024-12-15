"""
https://leetcode.com/problem-list/binary-tree/?difficulty=MEDIUM
URL: https://leetcode.com/problems/longest-univalue-path/submissions/1479705098/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_arr = right_arr = 0
            if node.left and node.left.val == node.val:
                left_arr = left_len + 1
            if node.right and node.right.val == node.val:
                right_arr = right_len + 1

            self.longest_path = max(self.longest_path, left_arr + right_arr)

            return max(left_arr, right_arr)

        dfs(root)
        return self.longest_path
