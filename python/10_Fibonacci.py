# 题目： 求斐波那契数列的第n项
# 写一个函数，输入n，求斐波那契数列的第n项

class Solution:

    def finonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1, f2 = 1, 0
        fn = 0
        for i in range(2, n + 1):
            fn = f1 + f2
            f2 = f1
            f1 = fn
        return fn

# 延伸题：
# 一、青蛙跳台阶
# 二、2x1 的小矩形覆盖 2xN 的大矩形
# 仍然都是斐波那契