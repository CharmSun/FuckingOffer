# 题目：数组中唯一只出现一次的数字
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
from typing import List


class Solution:
    # 对所有数的每一bit位，求和，然后对3求余就是只出现1次的数在当前位的值（0或1）。
    # 最后注意负数的情况
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit = 1 << i
            temp = 0
            for num in nums:
                if num & bit != 0:
                    temp += 1
            if temp % 3 != 0:
                res |= bit
        if res > 2**31 - 1:
            return res - 2**32
        return res


print(Solution().singleNumber([-1, -1, -1, -3]))
print(Solution().singleNumber([-3]))
