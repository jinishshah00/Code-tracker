"""
Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

Difficulty: Hard
Tags: Array, Binary Search
Solved: 2026-01-15T20:23:45Z
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m
            else:
                r -= 1
        
        return nums[l]
