"""
Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

Difficulty: Medium
Tags: Array, Binary Search
Solved: 2026-01-14T00:56:14Z
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:return True

            else: 
                if nums[mid] > nums[l]:
                    if nums[l] <= target <nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                elif nums[mid] < nums[l]:
                    if nums[mid] < target <= nums[r]:
                        l  = mid + 1
                    else: 
                        r = mid - 1
                else:
                    l = l+1
        
        return False
