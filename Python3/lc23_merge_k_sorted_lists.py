# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [] 

        #push first element of each list in min heap
        for i in range(len(lists)):
            if lists[i]:
                heappush(min_heap, [lists[i].val, i])

        if not min_heap:
            return None

        _, min_node_list = heappop(min_heap)

        res_head = lists[min_node_list]
        curr_node = res_head

        lists[min_node_list] = lists[min_node_list].next
        if lists[min_node_list]:
            heappush(min_heap, [lists[min_node_list].val, min_node_list])

        while(min_heap):
            _, min_node_list = heappop(min_heap)
            curr_node.next = lists[min_node_list]
            curr_node = curr_node.next

            lists[min_node_list] = lists[min_node_list].next
            if lists[min_node_list]:
                heappush(min_heap, [lists[min_node_list].val, min_node_list])


        return res_head