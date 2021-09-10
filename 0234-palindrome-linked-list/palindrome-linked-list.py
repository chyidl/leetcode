# Given the head of a singly linked list, return true if it is a palindrome.
#
#  
# Example 1:
#
#
# Input: head = [1,2,2,1]
# Output: true
#
#
# Example 2:
#
#
# Input: head = [1,2]
# Output: false
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the list is in the range [1, 105].
# 	0 <= Node.val <= 9
#
#
#  
# Follow up: Could you do it in O(n) time and O(1) space?


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev = None
        fast = head
        slow = head

        # Reverse half the list while trying to find the end
        while fast and fast.next:
            fast = fast.next.next
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # left side
        left = prev

        # right side
        if fast:
            """
            if fast is not None, then the length of the list is odd
            and we can ignore the middle value
            """
            right = slow.next
        else:
            right = slow

        # Just need to traverse each side and check if the value equal or not.
        while left is not None and right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

        
