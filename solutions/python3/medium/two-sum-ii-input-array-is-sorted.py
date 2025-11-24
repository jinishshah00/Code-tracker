"""
Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Difficulty: Medium
Tags: Array, Two Pointers, Binary Search
Solved: 2025-11-23T22:59:12Z
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]

        # while (numbers[l-1] + numbers[r-1]) != target:
        #     if (numbers[l-1] + numbers[r-1]) > target:
        #         r -= 1
        #     if (numbers[l-1] + numbers[r-1]) < target:
        #         l += 1
        
        # return [l,r]
