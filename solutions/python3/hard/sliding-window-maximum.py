"""
Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Difficulty: Hard
Tags: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue
Solved: 2026-01-30T23:44:23Z
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output
