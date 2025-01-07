"""
URL:https://leetcode.com/problems/reverse-linked-list/?envType=study-plan-v2&envId=leetcode-75

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative T: O(n), S: O(1)
        prev = None
        current = head

        while current:
            next_holder = current.next
            
            current.next = prev
            prev = current
            current = next_holder

        print(current)
        print(prev)

        # Return prev because current is tail of the list (which is None)
        # the thing before current/tail (prev) is the entire linked list that has been reversed
        return prev



        # # Recursive T: O(n), S: O(n)
        # # with most recursive functions do base case first
        # if not head:
        #     return None

        # new_head = head
        # if head.next:
        #     new_head = self.reverse_list(head.next)
        #     head.next.next = head
        # head.next = None

        # return new_head
