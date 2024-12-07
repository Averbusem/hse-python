"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/submissions/1472916681/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(
        self, preorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root

        left_root_val = preorder[1]
        left_subtree_size = postorder.index(left_root_val) + 1

        root.left = self.constructFromPrePost(
            preorder[1 : left_subtree_size + 1], postorder[:left_subtree_size]
        )
        root.right = self.constructFromPrePost(
            preorder[left_subtree_size + 1 :], postorder[left_subtree_size:-1]
        )

        return root
