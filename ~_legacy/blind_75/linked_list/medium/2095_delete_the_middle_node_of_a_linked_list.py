from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Tip: when we need a specific node in a singly linked list think of 2 pointers (or manually calcualte len)
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        length = 0
        start = head
        while start:
            length += 1
            start = start.next

        middle_index = length // 2

        position = head
        for _ in range(middle_index - 1):
            position = position.next

        position.next = position.next.next

        return head


        # TWO (THREE) POINTER SOLUTION 
        # slow = head
        # fast = head # moves twice as fast
        # pointer_previous = None # always 1 behind slow

        # while fast and fast.next:
        #     fast = fast.next.next
        #     pointer_previous = slow
        #     slow = slow.next

        # pointer_previous.next = slow.next
        # return head

        # INTUTION / CALCULATE MIDDLE INDEX SOLUTION