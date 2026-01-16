"""
Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/

Difficulty: Medium
Tags: Array, Binary Search, Sliding Window, Prefix Sum
Solved: 2026-01-15T23:41:15Z
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float('infinity')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min( r - l + 1, res)
                total -= nums[l]
                l += 1
        
        return 0 if res == float('infinity') else res
                