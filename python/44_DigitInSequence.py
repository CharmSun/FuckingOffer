# 题目：数字序列中某一位的数字
# 数字以0123456789101112131415…的格式序列化到一个字符序列中。
# 在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
# 请写一个函数，求任意第n位对应的数字。

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 0:
            return -1
        len_num = 1
        while True:
            count = self.countOfLenNums(len_num)
            if n < count * len_num:
                return self.digitAtLenNums(n, len_num)
            n -= count * len_num
            len_num += 1
        return -1

    # 长度为len的数有多少个
    def countOfLenNums(self, len: int):
        if len == 1:
            return 10
        return 9 * pow(10, len - 1)

    # 找到位于某len位数之中，找到具体数number，位于数number中的第index位（从左往右）
    def digitAtLenNums(self, n: int, len: int):
        begin = pow(10, len - 1) if len > 1 else 0
        number = begin + n // len
        index = n % len
        return int(str(number)[index])


print(Solution().findNthDigit(3))
