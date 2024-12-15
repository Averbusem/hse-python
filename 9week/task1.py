"""
https://leetcode.com/problem-list/binary-tree/
URL: https://leetcode.com/problems/validate-binary-search-tree/submissions/1472855804/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=-float("inf"), high=float("inf")):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root)
