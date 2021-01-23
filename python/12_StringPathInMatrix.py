# 题目：矩阵中的路径
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
# 字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中
# 上下左右移动一格，路径不能重复进入同一个格子。

from typing import List


class Solution:
    def hasPath(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        rows = len(board)
        cols = len(board[0])
        visited = [[False for j in range(cols)] for i in range(rows)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0, visited):
                    return True
        return False

    def dfs(self, board, i, j, word, charIdx, visited):
        if charIdx == len(word):
            return True
        if i < 0 or i >= len(board) \
                or j < 0 or j >= len(board[0]) \
                or word[charIdx] != board[i][j] \
                or visited[i][j]:
            return False
        visited[i][j] = True
        res = self.dfs(board, i+1, j, word, charIdx+1, visited) \
            or self.dfs(board, i-1, j, word, charIdx+1, visited) \
            or self.dfs(board, i, j+1, word, charIdx+1, visited) \
            or self.dfs(board, i, j-1, word, charIdx+1, visited)
        visited[i][j] = False
        return res


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
print(Solution().hasPath(board, word))
