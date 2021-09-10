# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#  
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
#
#  
# Constraints:
#
#
# 	1 <= n <= 8
#
#


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # solution: 数学归纳法
        # solution: recursion递归搜索 字符长度 2*n (2^2n)筛选 递归 
        # solution: 改进 左括号n 右括号n O(2^n)
        self.list = [] 
        self._gen(0, 0, n, "")
        return self.list 
    
    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.list.append(result)
            return 
        if left < n:
            self._gen(left+1, right, n, result + "(")
        if left > right and right < n:
            self._gen(left, right + 1, n, result + ")")
        
        
