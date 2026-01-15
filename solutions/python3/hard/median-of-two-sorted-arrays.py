"""
Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Difficulty: Hard
Tags: Array, Binary Search, Divide and Conquer
Solved: 2026-01-13T20:55:36Z
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A)+len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            m1 = (l+r)//2
            m2 = half - m1 - 2
            
            Aleft = A[m1] if m1 >= 0 else float("-infinity")
            Aright = A[m1+1] if (m1+1) < len(A) else float("infinity")
            Bleft = B[m2] if m2 >= 0 else float("-infinity")
            Bright = B[m2+1] if (m2+1) < len(B) else float("infinity")

            #partitions are correct or not
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total%2:
                    return min(Aright, Bright)
                #even
                else:
                    return (max(Aleft, Bleft)+min(Aright, Bright))/ 2
            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1
