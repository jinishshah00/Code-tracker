"""
Binary Search
https://leetcode.com/problems/binary-search/

Difficulty: Easy
Tags: Array, Binary Search
Solved: 2025-11-24T02:52:11Z
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        for i, v in enumerate(nums):
            if v == target:
                res = i
                break
            else:
                res = -1
        return res

        