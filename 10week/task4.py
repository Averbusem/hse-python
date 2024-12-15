"""
https://leetcode.com/problem-list/binary-tree/?difficulty=MEDIUM
URL: https://leetcode.com/problems/find-largest-value-in-each-tree-row/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            level_size = len(queue)
            max_value = float("-inf")

            for _ in range(level_size):
                node = queue.pop(0)

                max_value = max(max_value, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(max_value)

        return result
