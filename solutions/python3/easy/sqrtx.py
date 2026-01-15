"""
Sqrt(x)
https://leetcode.com/problems/sqrtx/

Difficulty: Easy
Tags: Math, Binary Search
Solved: 2026-01-13T21:19:33Z
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + ((r-l) // 2)
            if m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
                res = m
            else:
                return m

        return res