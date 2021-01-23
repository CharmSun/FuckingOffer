# 题目： 1~n 整数中1出现的次数
# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

class Solution:
    # 思路：每次去掉最高位进行递归
    # 最高位1的次数 + 其他位1的次数 + 递归的结果
    # 时间复杂度: O(logn)
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 9:
            return 1
        first = int(str(n)[0])
        other = int(str(n)[1:])
        l = len(str(n))
        numFirstDigit = 0
        if first > 1:
            numFirstDigit = pow(10, l-1)
        elif first == 1:
            numFirstDigit = other + 1
        numOtherDigits = first * (l-1) * pow(10, l-2)
        numRecursive = self.countDigitOne(other)
        return numFirstDigit + numOtherDigits + numRecursive