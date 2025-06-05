# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1


        if list1.val < list2.val:
            new_ll = list1
            list1 = list1.next
        else:
            new_ll = list2
            list2 = list2.next

        head = new_ll
        while list1 and list2:
            if list1.val < list2.val:
                new_ll.next = list1
                list1 = list1.next
            else:
                new_ll.next = list2
                list2 = list2.next
            new_ll = new_ll.next
        
        if list1:
            new_ll.next = list1

        if list2:
            new_ll.next = list2


        return head
        
    # Depends how you look at it. There is O(min(n,m)) work being done in my implementation but you could argue it is O(m+n) time because we "consider" the size of the input
    # Space O(1)
    # think "three pointers" or four technically
    # the pointer for the new llist, the pointer for list1, pointer for list2, and technically need a pointer for the head of the new llist