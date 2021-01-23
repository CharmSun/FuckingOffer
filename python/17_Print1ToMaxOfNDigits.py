# 题目： 打印从1到最大的n位数
# 输入数字n，按顺序打印从1到最大的n位十进制数。比如输入3，则
# 打印出1、2、3一直到最大的3位数999

class Solution:
    # 考虑大数问题，字符串来表示大数，用递归实现全排列
    def print1ToMaxOfNDigits(self, n: int):
        if n <= 0:
            return
        number = ['0'] * n
        self.helper(number, n, 0)
        
    def helper(self, number, n, index):
        if (index >= n):
            return
        for i in range(0, 10):
            number[index] = str(i)
            self.helper(number, n, index+1)
            if index == n - 1:
                self.printNumber(number)

    def printNumber(self, number):
        i = 0
        while i < len(number):
            if number[i] != '0':
                break
            i += 1
        if i < len(number):
            print(''.join(number[i:]))

Solution().print1ToMaxOfNDigits(3)
