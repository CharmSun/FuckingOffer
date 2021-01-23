# 题目：把数组排成最小的数
# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 输入: [10,2]
# 输出: "102"

# 说明:
# 输出结果可能非常大，所以你需要返回一个字符串而不是整数
# 拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0

from typing import List
from functools import cmp_to_key

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            str1 = str(a) + str(b)
            str2 = str(b) + str(a)
            if str1 < str2:
                return -1
            elif str2 > str1:
                return 1
            else:
                return 0
        strs = [str(num) for num in nums]
        strs.sort(key = cmp_to_key(cmp))
        return ''.join(strs)

print(Solution().minNumber([10, 2]))
