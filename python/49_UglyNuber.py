# 题目：丑数
# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
# 说明:
# 1 是丑数。
# n 不超过1690。

class Solution:
    # 利用已有丑数递推
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        uglyNums = [0] * n
        uglyNums[0] = 1
        i = 1
        t2 = t3 = t5 = 0
        while i < n:
            nextUgly = min(uglyNums[t2]*2, uglyNums[t3]*3, uglyNums[t5]*5)
            uglyNums[i] = nextUgly
            while uglyNums[t2] * 2 <= nextUgly:
                t2 += 1
            while uglyNums[t3] * 3 <= nextUgly:
                t3 += 1
            while uglyNums[t5] * 5 <= nextUgly:
                t5 += 1
            i += 1
        return uglyNums[n-1]
