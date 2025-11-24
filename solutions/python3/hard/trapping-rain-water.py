"""
Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/

Difficulty: Hard
Tags: Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack
Solved: 2025-11-24T01:42:47Z
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]

        return res
            


