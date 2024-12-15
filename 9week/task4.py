"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/add-one-row-to-tree/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import deque
from typing import Optional


# Определение класса узла бинарного дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        queue = deque([root])
        curr_depth = 1

        while queue:
            curr_depth += 1
            level_size = len(queue)

            for _ in range(level_size):
                node = queue.popleft()

                if curr_depth == depth:
                    old_left = node.left
                    old_right = node.right
                    node.left = TreeNode(val, old_left, None)
                    node.right = TreeNode(val, None, old_right)
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            if curr_depth == depth:
                break

        return root
