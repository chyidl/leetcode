// You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
//
// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
//
//  
// Example 1:
//
//
// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
//
//
// Example 2:
//
//
// Input: l1 = [0], l2 = [0]
// Output: [0]
//
//
// Example 3:
//
//
// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]
//
//
//  
// Constraints:
//
//
// 	The number of nodes in each linked list is in the range [1, 100].
// 	0 <= Node.val <= 9
// 	It is guaranteed that the list represents a number that does not have leading zeros.
//
//


/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/*
    解题思路:
        1. 创建新的链表存储合并后的结果 result
        2. 遍历输入l1, l2链表数值 并相加保存到 carry
        3. 对相加后的结果carry求余 赋值result
    
    时间复杂度: O(m + n)
    空间复杂度: O(m + n)
*/
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// 初始化余数,结果集
	carry, result := 0, new(ListNode)
	for node := result; l1 != nil || l2 != nil || carry > 0; node = node.Next {
		if l1 != nil {
			carry += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			carry += l2.Val
			l2 = l2.Next
		}
		node.Next = &ListNode{carry % 10, nil}
		carry /= 10
	}
	return result.Next
}

