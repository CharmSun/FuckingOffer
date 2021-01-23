# 题目： 机器人的运动范围
# 地上有一个m行n列的方格。一个机器人从坐标（0，0）的格子开始移动
# 每次可以向左右上下移动一格，但不能进入行坐标和列坐标的数位之和大于
# k的格子。例如，当k为18时，能进入方格（35，37），但不能进入方格
# （35，38）。请问该机器人能够到达多少个格子？

class Solution:
    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        if (threshold < 0 or rows <= 0 or cols <= 0):
            return 0
        visited = [[False for j in range(cols)] for i in range(rows)]
        res = self.dfs(threshold, rows, cols, 0, 0, visited)
        return res
    
    def dfs(self, threshold, rows, cols, i, j, visited) -> int:
        count = 0
        if self.check(threshold, rows, cols, i, j, visited):
            visited[i][j] = True
            count = 1 + self.dfs(threshold, rows, cols, i-1, j, visited) \
                    + self.dfs(threshold, rows, cols, i+1, j, visited) \
                    + self.dfs(threshold, rows, cols, i, j-1, visited) \
                    + self.dfs(threshold, rows, cols, i, j+1, visited)

        return count

    def check(self, threshold, rows, cols, i, j, visited) -> bool:
        sum = self.getDigitSum(i) + self.getDigitSum(j)
        if i >= 0 and i < rows \
            and j >= 0 and j < cols \
            and sum <= threshold \
            and not visited[i][j]:
            return True
        return False
    
    def getDigitSum(self, number: int) -> int:
        sum = 0
        while number > 0:
            sum += number % 10
            number /= 10
        return sum
