# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        # we will try with two passes
        # first to get the length of the linked list
        length = 0

        while curr:
            curr = curr.next
            length += 1
        
        remove_index = length - n
        if remove_index == 0:
            return head.next

        cur = head
        for i in range(length - 1):
            if (i + 1) == remove_index:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head

        
        