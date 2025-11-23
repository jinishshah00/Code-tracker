/**
 * Find the Index of the First Occurrence in a String
 * https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
 * 
 * Difficulty: Easy
 * Tags: Two Pointers, String, String Matching
 * Solved: 2025-02-21T10:38:53Z
 */

class Solution {
public:
    int strStr(string haystack, string needle) {
        size_t pos = haystack.find(needle);
        return (pos != std::string::npos) ? pos : -1;
    }
};