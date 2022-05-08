// Given the head of a linked list, return the list after sorting it in ascending order.
//
//  
// Example 1:
//
//
// Input: head = [4,2,1,3]
// Output: [1,2,3,4]
//
//
// Example 2:
//
//
// Input: head = [-1,5,3,4,0]
// Output: [-1,0,3,4,5]
//
//
// Example 3:
//
//
// Input: head = []
// Output: []
//
//
//  
// Constraints:
//
//
// 	The number of nodes in the list is in the range [0, 5 * 104].
// 	-105 <= Node.val <= 105
//
//
//  
// Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
//


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func sortList(head *ListNode) *ListNode {
	// 快排 -- 只有一个节点不需要排序
	if head == nil || head.Next == nil {
		return head
	}

	l, r := head, head
	for r != nil && r.Next != nil && r.Next.Next != nil {
		l, r = l.Next, r.Next.Next
	}

	r = l.Next
	l.Next = nil
	l = head

	// 递归
	l, r = sortList(l), sortList(r)
    
    // header
	h := &ListNode{}
    // tail
	t := h
	for l != nil && r != nil {
		if l.Val < r.Val {
			t.Next = l
			l = l.Next
		} else {
			t.Next = r
			r = r.Next
		}
		t = t.Next
	}
	if l != nil {
		t.Next = l
	}
	if r != nil {
		t.Next = r
	}

	return h.Next
}

