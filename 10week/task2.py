"""
https://leetcode.com/problem-list/binary-tree/?difficulty=MEDIUM
URL: https://leetcode.com/problems/path-sum-ii/submissions/1479693868/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, cur_path, cur_sum):
            if not node:
                return

            cur_path.append(node.val)
            cur_sum += node.val

            if not node.left and not node.right and cur_sum == targetSum:
                result.append(list(cur_path))
            else:
                dfs(node.left, cur_path, cur_sum)
                dfs(node.right, cur_path, cur_sum)

            cur_path.pop()

        dfs(root, [], 0)
        return result
