# 题目：不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。


class Solution:
    # 不考虑进位，每位相加为sum, 用异或求得
    # 求进位，两个数先做位与，再左移一位
    # 重复sum+carry, 直到carry 为0
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff  # python 超过32位数，用来转为32位整数
        a, b = a & x, b & x
        sum = a ^ b
        carry = ((a & b) << 1) & x
        while carry:
            num1 = sum
            num2 = carry
            sum = num1 ^ num2
            carry = ((num1 & num2) << 1) & x
        if sum > 0x7fffffff:  # 2**31 - 1
            return ~(sum ^ x)  # 负数时，将32以上的高位转为1
        return sum


print(Solution().add(-1, 2))
