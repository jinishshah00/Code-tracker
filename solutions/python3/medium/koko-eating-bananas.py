"""
Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Difficulty: Medium
Tags: Array, Binary Search
Solved: 2025-11-26T00:30:14Z
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r)//2
            sH = self.sumHours(piles, mid) 
            if sH <= h:
                res = mid
                r = mid - 1
            elif sH > h:
                l = mid + 1

        return res

    
    def sumHours(self, piles: List[int], k: int) -> int:
        Sum = 0
        for i in piles:
            Sum += (i+k-1)//k
        return Sum