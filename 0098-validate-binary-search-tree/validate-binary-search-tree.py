# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
#
# 	The left subtree of a node contains only nodes with keys less than the node's key.
# 	The right subtree of a node contains only nodes with keys greater than the node's key.
# 	Both the left and right subtrees must also be binary search trees.
#
#
#  
# Example 1:
#
#
# Input: root = [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [1, 104].
# 	-231 <= Node.val <= 231 - 1
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Solution: In-order 中序遍历 -- 升序 
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))
    
    def inorder(self, root):
        if root is None:
            return [] 
        # 左 根 右 
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    
    
    # Solution: Recurision: 递归函数 
    # 左子树取最大值 max 右子树取最小值 min  
    # 判断 max < root; root > min 
        
        
