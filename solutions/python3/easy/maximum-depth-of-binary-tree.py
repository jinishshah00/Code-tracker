"""
Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Difficulty: Easy
Tags: Tree, Depth-First Search, Breadth-First Search, Binary Tree
Solved: 2026-02-05T01:16:08Z
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS

        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # -----------------------------------------------------------------------  
        # if not root:
        #     return 0
        
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         root = q.popleft()
        #         if root.left:
        #             q.append(root.left)
        #         if root.right:
        #             q.append(root.right)
        #     level += 1

        # return level

        #Iterative DFS
        stack = [[root,1]]
        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res


