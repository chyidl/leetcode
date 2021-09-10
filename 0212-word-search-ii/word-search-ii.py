# Given an m x n board of characters and a list of strings words, return all words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#  
# Example 1:
#
#
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#  
# Constraints:
#
#
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 12
# 	board[i][j] is a lowercase English letter.
# 	1 <= words.length <= 3 * 104
# 	1 <= words[i].length <= 10
# 	words[i] consists of lowercase English letters.
# 	All the strings of words are unique.
#
#


END_OF_WORD = "#"
# 方向数组
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 
        if not board or not board[0]: return [] 
        if not words: return []

        self.result = set() 
        
        # 有序字典 - Trie 
        root = collections.defaultdict() 
        # words 字典加入Trie 
        for word in words:
            node = root 
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD 
        
        # board row col 
        self.m, self.n = len(board), len(board[0])
        
        # 遍历board 
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        
        return self.result 

                    
    def _dfs(self, board, i, j, cur_word, cur_dict):        
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        
        # 标记是否访问过 
        tmp, board[i][j] = board[i][j], "@"
        
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp 
        
