# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        curr = head
        prev = None
        while (i <left):
            prev = curr
            curr = curr.next
            i +=1
        if prev:
            prev.next = self.reverse(curr, right-left)
        else:
            head = self.reverse(curr, right-left)
        return head

    def reverse(self, head: Optional[ListNode], k:int) -> Optional[ListNode]:
        prev = None
        curr = head
        nex = head
        tail = head
        i = 1
        while(i <= k):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            i +=1
        tail.next = curr.next
        if prev:
            curr.next = prev

        return curr