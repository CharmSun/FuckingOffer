# 题目：正则表达式匹配
# 请实现一个函数用来匹配'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
# 而'*'表示它前面的字符可以出现任意次。

class Solution:
    # 递归解法
    def match(self, str: str, pattern: str) -> bool:
        if str == None or pattern == None:
            return False
        return self.matchCore(str, pattern, 0, 0)

    def matchCore(self, str, pattern, i, j) -> bool:
        # 如果模式先遍历完，则一定不匹配；如果同时遍历完，则一定匹配；
        if j == len(pattern):
            return i == len(str) 
        if j < len(pattern) - 1 and pattern[j+1] == '*':
            # 如果模式下一个为'*'，且当前匹配；
            if i < len(str) and (str[i] == pattern[j] or pattern[j] == '.'):
                # 模式后移两位，或者模式不变，字符串后移一位；（书中解法有重复计算）
                return self.matchCore(str, pattern, i, j+2) or \
                    self.matchCore(str, pattern, i+1, j)
            else:
                return self.matchCore(str, pattern, i, j+2)
        if i < len(str) and j < len(pattern) and \
                (str[i] == pattern[j] or pattern[j] == '.'):
            return self.matchCore(str, pattern, i+1, j+1)
        return False

    # dp解法， dp[i][j]表示s[0,i)和p[0,j)是否match，s长度i, p 长度j
    def dp_match(self, str: str, pattern: str) -> bool:
        m, n = len(str), len(pattern)
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if j > 1 and pattern[j-1] == '*':
                    if i > 0 and (str[i-1] == pattern[j-2] or pattern[j-2] == '.'):
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                elif i > 0 and (str[i-1] == pattern[j-1] or pattern[j-1] == '.'):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        return dp[m][n]



print(Solution().match("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))
