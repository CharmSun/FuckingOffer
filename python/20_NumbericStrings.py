# 题目：表示数值的字符串
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，
# 但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

class Solution:

    # 数字的格式 可用 A[.[B]][e|EC] 或者 .B[e|EC] 表示，A、C可以为正负整数，B是无符号整数
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        s = s.strip()
        if len(s) == 0:
            return False
        i = 0

        def scanUnsignedInt() -> bool:
            nonlocal i
            j = i
            while i < len(s) and s[i] >= '0' and s[i] <= '9':
                i += 1
            return i > j

        def scanInt() -> bool:
            nonlocal i
            if i < len(s) and (s[i] == '+' or s[i] == '-'):
                i += 1
            return scanUnsignedInt()

        numberic = scanInt()
        if i < len(s) and s[i] == '.':
            i += 1
            # .123 或 233. 都符合条件
            numberic = scanUnsignedInt() or numberic
        if i < len(s) and (s[i] == 'e' or s[i] == 'E'):
            i += 1
            # e 或 E的前面需要数字，后面需要为整数
            numberic = numberic and scanInt()
        return numberic and i == len(s)


print(Solution().isNumber('-1E-16'))
