"""
Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Difficulty: Medium
Tags: Array, Binary Search, Matrix
Solved: 2025-11-25T23:11:16Z
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1 = 0
        r1 = len(matrix)-1
        l2 = 0
        r2 = len(matrix[0])-1

        while l1 <= r1:
            mid1 = (l1+r1)//2
            if target == matrix[mid1][l2] or target == matrix[mid1][r2]:
                return True
            elif target < matrix[mid1][l2]:
                r1 = mid1 - 1
            elif target < matrix[mid1][r2] and target > matrix[mid1][l2]:
                while l2 <= r2:
                    mid2 = (l2+r2)//2
                    if target == matrix[mid1][mid2]:
                        return True
                    elif target < matrix[mid1][mid2]:
                        r2 = mid2 - 1
                    elif target > matrix[mid1][mid2]:
                        l2 = mid2 + 1
            elif target > matrix[mid1][r2]:
                l1 = mid1 + 1

        return False

