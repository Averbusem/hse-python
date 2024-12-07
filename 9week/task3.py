"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/path-sum-iii/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val

            count = prefix_sums[current_sum - targetSum]

            prefix_sums[current_sum] += 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sums[current_sum] -= 1

            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # для случая, когда путь равен targetSum

        return dfs(root, 0)
