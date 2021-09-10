# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
#
#  
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#  
# Constraints:
#
#
# 	The number of nodes in the tree is in the range [0, 2000].
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS: 广度搜索优先 batch process  O(n) 
#         if not root:return []
        
#         stack,queue,res,nCount=[root],[],[[root.val]],1
        
#         # visited = set(root) 
        
#         while stack:
#             temp=stack.pop(0)
#             if temp.left:
#                 stack.append(temp.left)
#             if temp.right:
#                 stack.append(temp.right)
#             nCount-=1
#             if nCount==0:
#                 queue=[x.val for x in stack]
#                 res+=[queue] if queue else []
#                 nCount=len(stack)
#         return res
    
        # DFS: 深度搜索优先 level info 
        if not root: return []
        self.result = [] 
        self._dfs(root, 0)
        return self.result 
    
    def _dfs(self, node: TreeNode, level: int):
        if not node: return 
        
        if len(self.result) < level + 1:
            self.result.append([])
        
        self.result[level].append(node.val)
        
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
        
        
