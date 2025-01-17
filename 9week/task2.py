"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result[::-1]
