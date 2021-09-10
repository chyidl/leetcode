# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#
#
# Example 2:
#
#
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 105].
# 	-1000 <= Node.val <= 1000
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # Solution: BFS 
        # if root is None: return 0
        # min_level = 1 
        # queue = [root]
        # count = 1
        # while queue:
        #     tmp = queue.pop(0)
        #     if tmp.left is None and tmp.right is None:
        #         return min_level 
        #     if tmp.left:
        #         queue.append(tmp.left)
        #     if tmp.right:
        #         queue.append(tmp.right)
        #     count -= 1
        #     if count == 0:
        #         count = len(queue)
        #         min_level += 1 
        # return min_level
        
        # Solution DFS: 
#         if root is None: return 0
#         if root.left is None:
#             return 1 + self.minDepth(root.right)
#         if root.right is None:
#             return 1 + self.minDepth(root.left)
        
#         # divide and conquer 
#         leftMinDepth = self.minDepth(root.left)
#         rightMinDepth = self.minDepth(root.right)
        
#         # process subproblem results
#         result = 1 + min(leftMinDepth, rightMinDepth)
#         return result
        
        # Solution DFS2:
        if root is None: return 0 
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1
