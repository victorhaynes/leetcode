from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Step 1 calculate middle using fast/slow pointers. Slow is the middle (cheated to the right)
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow)


        # Step 2 reverse the 1st half of the linked list
        prev = None
        current = head

        while current and current != slow:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        # print(prev) # remember prev is the head of a reversed list, not head


        # Step 3 Iterate through now with your head (prev) and the middle (slow)
        twin_max = 0
        while prev and slow:
            twin_max = max(twin_max, prev.val + slow.val)
            prev = prev.next
            slow = slow.next

        return twin_max