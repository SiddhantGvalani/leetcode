# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        sz = 0
        while curr:
            sz += 1
            curr = curr.next
        if (sz - n) == 0:
            return head.next
        else:
            curr = head
            node = 1
            while node != (sz - n):
                node += 1
                curr = curr.next
        temp = curr.next
        curr.next = temp.next
        temp.next = None
        return head
