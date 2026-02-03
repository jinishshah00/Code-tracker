"""
Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/

Difficulty: Medium
Tags: Array, Two Pointers, Binary Search, Bit Manipulation
Solved: 2026-02-02T20:21:02Z
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

        
