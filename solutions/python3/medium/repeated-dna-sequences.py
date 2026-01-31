"""
Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/

Difficulty: Medium
Tags: Hash Table, String, Bit Manipulation, Sliding Window, Rolling Hash, Hash Function
Solved: 2026-01-30T22:54:39Z
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for l in range(len(s) - 9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return list(res)