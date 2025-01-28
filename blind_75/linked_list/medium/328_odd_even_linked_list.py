from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next: # if no head, ll len(1) or ll len(2) then return head bc it is the solution
            return head

        odd_pointer = head # i = 1 case
        even_pointer = head.next # i = 2 case
        even_head = even_pointer # need to store this so we can link the tail of the odd sllist to the head of the even sllist
        current = head # traversal tool

        i = 1
        while current:
            if i > 2: # only do work if we are on the 3rd node or more
                if i % 2 != 0: # if odd node - update odd pointer's next
                    odd_pointer.next = current
                    odd_pointer = odd_pointer.next
                else: # if even node - update even pointer's next
                    even_pointer.next = current
                    even_pointer = even_pointer.next
            current = current.next
            i += 1

        even_pointer.next = None # set the tail to None, the last even node is the end of the sllist
        odd_pointer.next = even_head

        return head

