/**
 * Pascal's Triangle II
 * https://leetcode.com/problems/pascals-triangle-ii/
 * 
 * Difficulty: Easy
 * Tags: Array, Dynamic Programming
 * Solved: 2025-02-19T13:05:59Z
 */

class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> res(1,1);
        long long prev = 1;
        for (int k = 1; k <= rowIndex; ++k) {
            long long curr = prev * (rowIndex-k+1)/k;
            res.push_back(curr);
            prev = curr;
        }
        return res;
    }
};