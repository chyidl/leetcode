# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        heapq.heapify(heap)
        head = ListNode(float("inf"))
        tail = head 
        [heapq.heappush(heap, (v.val, i)) for i, v in enumerate(lists) if v]
        while heap:
            curVal, curIndex = heapq.heappop(heap)
            curHead = lists[curIndex]
            curNext = curHead.next 
            tail.next = curHead
            curHead.next = None 
            tail = curHead
            curHead = curNext
            if curHead:
                lists[curIndex] = curHead 
                heapq.heappush(heap, (curHead.val, curIndex))
        return head.next 
