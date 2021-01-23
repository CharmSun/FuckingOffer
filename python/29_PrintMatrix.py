# 题目：顺时针打印矩阵
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
from typing import List


class Solution:

    # 注意条件判断
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]:
            return res
        startY, endY = 0, len(matrix) - 1
        startX, endX = 0, len(matrix[0]) - 1
        while startY <= endY and startX <= endX:
            for i in range(startX, endX+1):
                res.append(matrix[startY][i])
            startY += 1
            if startY <= endY:
                for i in range(startY, endY+1):
                    res.append(matrix[i][endX])
                endX -= 1
            if startY <= endY and startX <= endX:
                for i in range(endX, startX-1, -1):
                    res.append(matrix[endY][i])
                endY -= 1
            if startY <= endY and startX <= endX:
                for i in range(endY, startY-1, -1):
                    res.append(matrix[i][startX])
                startX += 1
        return res


matrix = [[1, 2], [3, 4]]
print(Solution().spiralOrder(matrix))
