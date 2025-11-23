/**
 * Merge Sorted Array
 * https://leetcode.com/problems/merge-sorted-array/
 * 
 * Difficulty: Easy
 * Tags: Array, Two Pointers, Sorting
 * Solved: 2025-03-01T23:37:32Z
 */

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        for (int i = 0; i < n; i++) {
            nums1[m+i] = nums2[i];
        }
        sort(nums1.begin(), nums1.end());
    }
};