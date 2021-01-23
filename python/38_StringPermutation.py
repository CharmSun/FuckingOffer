# 题目：字符串的排列
# 输入一个字符串，打印出该字符串中字符的所有排列。
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
from typing import List


class Solution:
    # 1、固定第一位所有可能值，后面的递归全排列
    # 2、处理当前位时，注意去重，做剪枝
    def permutation(self, s: str) -> List[str]:
        if not s:
            return []
        s_list = list(s)
        res = []

        def dfs(i):
            if i == len(s_list) - 1:
                res.append(''.join(s_list))
                return
            dic = set()
            for k in range(i, len(s_list)):
                if s_list[k] in dic:
                    continue
                dic.add(s_list[k])
                s_list[i], s_list[k] = s_list[k], s_list[i]
                dfs(i+1)
                s_list[i], s_list[k] = s_list[k], s_list[i]
        dfs(0)
        return res

# 拓展1：求字符的所有组合，例如输入三个字符a,b,c，则组合有a,b,c,ab,ac,bc,abc


class Solution1:
    def subsetsWithDup(self, s: str) -> List[str]:
        if not s:
            return []
        output = []
        ans = []
        s_list = sorted(s)
        self.dfs(s_list, 0, ans, output)
        return output

    def dfs(self, s_list, pos, ans, output):
        for i in range(pos, len(s_list)):
            if i > pos and s_list[i] == s_list[i-1]:
                continue
            ans.append(s_list[i])
            output.append(''.join(ans))
            self.dfs(s_list, i+1, ans, output)
            ans.pop()


# res = Solution().permutation('lssuv')
# print(len(res))
# print(len(set(res)))
print(Solution1().subsetsWithDup('abb'))


# 拓展2：n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queen = [['.'] * n for i in range(n)]
        def queen2Str(queen):
            l = []
            for row in queen:
                l.append(''.join(row))
            return l

        def isValid(queen, row, col):
            for i in range(row):
                for j in range(n):
                    if queen[i][j] == 'Q' and (j == col or abs(i-row) == abs(j-col)):
                        return False
            return True

        def backtrack(queen, row):
            if row == n:
                res.append(queen2Str(queen))
                return
            for col in range(n):
                if isValid(queen, row, col):
                    queen[row][col] = 'Q'
                    backtrack(queen, row+1)
                    queen[row][col] = '.'

        backtrack(queen, 0)
        return res


# 拓展3：n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

class Solution3:

    def totalNQueens(self, n: int) -> int:
        queen = [-1] * n # 存棋盘每行皇后的列位置
        res = 0

        def isValid(queen, row):
            for i in range(row):
                if queen[i] == queen[row] or abs(row - i) == abs(queen[row] - queen[i]):
                    return False
            return True
        
        def backtrack(row):
            if row == n:
                nonlocal res
                res += 1
                return
            for col in range(n):
                queen[row] = col
                if isValid(queen, row):
                    backtrack(row + 1)
        backtrack(0)
        return res

input = 1
print(Solution3().totalNQueens(input))
