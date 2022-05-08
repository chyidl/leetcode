// You are given the heads of two sorted linked lists list1 and list2.
//
// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
//
// Return the head of the merged linked list.
//
//  
// Example 1:
//
//
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
//
//
// Example 2:
//
//
// Input: list1 = [], list2 = []
// Output: []
//
//
// Example 3:
//
//
// Input: list1 = [], list2 = [0]
// Output: [0]
//
//
//  
// Constraints:
//
//
// 	The number of nodes in both lists is in the range [0, 50].
// 	-100 <= Node.val <= 100
// 	Both list1 and list2 are sorted in non-decreasing order.
//
//


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	res := &ListNode{}
	cur := res
	for l1 != nil || l2 != nil {
		if l1 == nil {
			cur.Next = l2
			l2 = nil
			continue
		}
		if l2 == nil {
			cur.Next = l1
			l1 = nil
			continue
		}

		if l1.Val > l2.Val {
			cur.Next = l2
			l2 = l2.Next
			cur = cur.Next
		} else {
			cur.Next = l1
			cur = cur.Next
			l1 = l1.Next
		}
	}
	return res.Next
}

