"""
Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Solved: 2026-02-04T23:22:34Z
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root