# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#  
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [0, 100].
# 	0 <= Node.val <= 100
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Solution: 递归
        # if head and head.next:
        #     temp = head.next
        #     head.next, temp.next = self.swapPairs(temp.next), head
        #     return temp
        # else:
        #     return head
        
        # Solution: 
        dummy = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next
