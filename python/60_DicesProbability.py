# 题目：n个骰子的点数
# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
from typing import List


class Solution:
    # n 个骰子，prob1 和 prob2 交替计算
    # prob2 中点数和为s 的次数，为prob1 中s-1,s-2,s-3,s-4,s-5,s-6 六个之和
    def dicesProbability(self, n: int) -> List[float]:
        if n < 1:
            return []
        minS, maxS = n, 6 * n
        prob1 = [0] * (maxS + 1)
        prob2 = [0] * (maxS + 1)
        for s in range(1, 7):
            prob1[s] = 1
        for k in range(2, n+1):
            for s in range(k):
                prob2[s] = 0
            for s in range(k, 6 * k + 1):
                prob2[s] = 0
                j = 1
                while j <= 6 and s-j >= 1:
                    prob2[s] += prob1[s-j]
                    j += 1
            prob1, prob2 = prob2, prob1
        total = pow(6, n)
        res = []
        for i in range(minS, maxS + 1):
            res.append(round(prob1[i] / total, 5))
        return res


print(Solution().dicesProbability(2))
