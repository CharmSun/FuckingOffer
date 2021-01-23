# 题目： 把数字翻译成字符串
# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，
# ……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 动态规划
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 0:
            return 0
        num_str = str(num)
        l = len(num_str)
        dp = [0] * l
        for i in range(l):
            if i == 0:
                dp[i] = 1
            else:
                last2Num = int(num_str[i-1:i+1])
                if last2Num >= 10 and last2Num <= 25:
                    dp[i] = dp[i-2] + dp[i-1] if i >= 2 else 1 + dp[i-1]
                else:
                    dp[i] = dp[i-1]
        return dp[l-1]

print(Solution().translateNum(12258))
