# 题目：圆圈中最后剩下的数字
# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
# 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

class Solution:
    # 约瑟夫环问题
    # 数学递推公式：f(n, m) = [f(n-1, m) + m] % n （n > 1）;   f(n, m) = 0 (n=1)
    # f(n, m) 表示n个数字每次删除第m个数字最后剩下的数字
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n+1):
            last = (last + m) % i
        return last
