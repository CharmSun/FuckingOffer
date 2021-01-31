# 题目：股票的最大利润
# 假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
# 输入: [7,1,5,3,6,4]
# 输出: 5
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min = prices[0]
        maxDiff = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] > min:
                maxDiff = max(maxDiff, prices[i] - min)
        return maxDiff


print(Solution().maxProfit([7, 6, 4, 3, 1]))
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
