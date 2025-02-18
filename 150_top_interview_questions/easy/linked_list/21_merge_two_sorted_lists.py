from typing import Optional, ListNode
"""
URL: https://leetcode.com/problems/merge-two-sorted-lists/description/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

# Time O(n) where n is the larger of the 2 linked list
# Space O(1) no extra memory used/does not scale with the size of n
# Takeaways: remember that "list1" and "list2" are list nodes....not exactly the entire list but a node with a reference to what is next
# also remember that head & current point to the same object/linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
                current = current.next

                current.next = list2
                list2 = list2.next
                
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2


        # print(head.next)
        return head.next