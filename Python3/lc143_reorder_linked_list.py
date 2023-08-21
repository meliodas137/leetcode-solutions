# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = slow.next
        if not fast:
            return head
        while(fast.next and fast.next.next):
           slow = slow.next
           fast  = fast.next.next
        if fast.next:
            slow = slow.next

        new_head = slow.next
        slow.next = None

        sec = self.reverse(new_head)

        #merge
        i = head
        while(sec):
            f_nex = i.next
            s_nex = sec.next

            i.next = sec
            sec.next = f_nex
            i = f_nex
            sec = s_nex

        return head
        

    def reverse(self, head):
        curr = head
        prev = None
        while(curr):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        return prev