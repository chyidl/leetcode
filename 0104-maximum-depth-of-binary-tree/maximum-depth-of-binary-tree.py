# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#
#
# Example 2:
#
#
# Input: root = [1,null,2]
# Output: 2
#
#
# Example 3:
#
#
# Input: root = []
# Output: 0
#
#
# Example 4:
#
#
# Input: root = [0]
# Output: 1
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 104].
# 	-100 <= Node.val <= 100
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Solution: BFS 广度优先搜索 O(n)
        # max_level = 0
        # if not root: return max_level 
        # queue = [root]
        # count = 1
        # while queue:
        #     tmp = queue.pop(0)
        #     if tmp.left:
        #         queue.append(tmp.left)
        #     if tmp.right:
        #         queue.append(tmp.right)
        #     count -= 1
        #     if count == 0:
        #         count = len(queue)
        #         max_level +=1
        # return max_level 
    
        # Solution: DFS 深度优先搜索 level info 更新 max min 
        if not root: return 0 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
