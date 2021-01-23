# 题目：剪绳子
# 给一根长度为n的绳子，请把绳子剪成m段（n>1,m>1），每段
# 绳子的长度记为k[0],k[1],...,k[m]。求k[0]*k[1]*...*k[m]
# 的可能的最大乘积。例如当绳子长度为8时，剪成2、3、3三段，最大乘积是18。

# 动态规划特点一：求一个问题的最优解
# 特点二： 整体问题的最优解是依赖各个子问题的最优解
# 特点三： 小问题之间还有相互重叠的更小的子问题
# 特点四： 从上往下分析问题，从下往上求解问题

class Solution:

    # 动态规划
    def maxProduct1(self, n: int) -> int:
        if n < 2:
            return 0
        # 长度为2，剪成1+1
        if n == 2:
            return 1
        # 长度为3，剪成1+2
        if n == 3:
            return 2
        # 数组中第i个元素表示把长度为i 的绳子剪成若干段之后各段长度乘积的最大值
        products = [0] * (n+1)
        products[1] = 1
        products[2] = 2
        products[3] = 3
        for i in range(4, n+1):
            max = 0
            for j in range(1, i // 2 + 1):
                product = products[j] * products[i-j]
                if max < product:
                    max = product
            products[i] = max

        return products[n]

    # 贪婪算法：当 n >= 5时，尽可能多地剪长度为3的绳子，当剩下的绳子长度为4时，剪成两段2
    def maxProduct2(self, n: int) -> int:
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        # 尽可能多地剪长度3
        timesOf3 = n // 3
        # 当剩下的长度为4，不能再剪长度3
        if n - timesOf3 * 3 == 1:
            timesOf3 -= 1
        timesOf2 = (n - timesOf3 * 3) // 2
        return pow(3, timesOf3) * pow(2, timesOf2)


print(Solution().maxProduct1(8))
print(Solution().maxProduct2(8))
