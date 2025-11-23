"""
Container With Most Water
https://leetcode.com/problems/container-with-most-water/

Difficulty: Medium
Tags: Array, Two Pointers, Greedy
Solved: 2025-09-07T16:59:07Z
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height)-1

        while left < right:

            res = max (res, (right-left) * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res