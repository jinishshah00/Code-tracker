/**
 * Remove Element
 * https://leetcode.com/problems/remove-element/
 * 
 * Difficulty: Easy
 * Tags: Array, Two Pointers
 * Solved: 2025-02-19T10:10:16Z
 */

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        vector<int> res;
        for (const auto& num : nums) {
            if (num != val) {
                res.push_back(num);
                k++;
            } 
        }
        for (int i = 0; i < k; ++i) {
            nums[i] = res[i];
        }
        return k;
    }
};