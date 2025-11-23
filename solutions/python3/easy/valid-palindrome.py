"""
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Difficulty: Easy
Tags: Two Pointers, String
Solved: 2025-09-07T18:46:37Z
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(chars)-1
        res = True
        while left <= right:
            if chars[left] == chars[right]:
                left += 1
                right -= 1
            else:
                res = False
                break
        return res