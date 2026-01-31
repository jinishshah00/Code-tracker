"""
Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/

Difficulty: Easy
Tags: Hash Table, Linked List, Two Pointers
Solved: 2026-01-31T18:49:57Z
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False