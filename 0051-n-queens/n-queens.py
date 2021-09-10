# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#  
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#
#
# Example 2:
#
#
# Input: n = 1
# Output: [["Q"]]
#
#
#  
# Constraints:
#
#
# 	1 <= n <= 9
#
#


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 西洋棋皇后 - 攻击范围米字形攻击
        # solution: DFS 深度优先搜索 递归 
        # queens: 皇后的位置 col 
        # xy_dif: (x, y) x-y 
        # xy_sum: (x, y) x+y 
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
