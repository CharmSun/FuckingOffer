# 题目：构建乘积数据
# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
# 即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        if n < 2:
            return []
        b = [1] * n
        for i in range(1, n):
            b[i] = b[i-1] * a[i-1]  # 从前向后累乘
        temp = 1
        for i in range(n-2, -1, -1):
            temp *= a[i+1]  # 从后向前累乘
            b[i] *= temp  # 前后两部分相乘
        return b


print(Solution().constructArr([1, 2, 3, 4, 5]))
