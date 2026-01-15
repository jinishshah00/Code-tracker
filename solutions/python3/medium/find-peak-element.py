"""
Find Peak Element
https://leetcode.com/problems/find-peak-element/

Difficulty: Medium
Tags: Array, Binary Search
Solved: 2026-01-15T21:11:22Z
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if m > 0 and nums[m-1] > nums[m]:
                r = m - 1
            elif m < r  and nums[m+1] > nums[m]:
                l = m + 1
            else:
                return m
                
                