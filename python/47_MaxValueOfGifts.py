# 题目： 礼物的最大价值
# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
# 你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
# 给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxValues = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValues[j]
                if j > 0:
                    left = maxValues[j-1]
                maxValues[j] = max(up, left) + grid[i][j]
        return maxValues[cols-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(Solution().maxValue(grid))
