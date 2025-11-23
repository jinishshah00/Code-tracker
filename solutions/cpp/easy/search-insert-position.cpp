/**
 * Search Insert Position
 * https://leetcode.com/problems/search-insert-position/
 * 
 * Difficulty: Easy
 * Tags: Array, Binary Search
 * Solved: 2025-03-01T23:12:13Z
 */

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int i;
        for (i = 0; i < nums.size(); ++i) {
            if (nums[i] >= target) {
                return i;
            }
        }
        return i;
    }
};