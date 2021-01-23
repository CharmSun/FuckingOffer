# 题目：数值的整数次方
# 实现函数power

class Solution:
    # 3 ** 10 == 9 ** 5 == （81 ** 2）* 9
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        while n > 0:
            if n & 1 == 1:
                res *= x
            x *= x
            n = n >> 1
        return round(res, 5)


x = 2.00000
n = -2
print(Solution().myPow(x, n))
