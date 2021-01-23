# 题目： 二进制中1的个数
# 实现一个函数，输入一个整数，输出该数二进制表示中1的个数

# 常规解法： 把n与1做与运算，然后反复左移1
# 惊喜解法：把一个整数减去1，再和原整数做与运算，会把该整数最右边的1变成0
#          一个整数的二进制中有多少个1，就可以进行多少从这样的操作。
class Solution:

    def numberOf1(self, n: int) -> int:
        count = 0
        while n > 0:
            count += 1
            n = (n - 1) & n
        return count

print(Solution().numberOf1(9))