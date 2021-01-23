# 题目：调整数组顺序使奇数位于偶数前面
# 输入一个数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分
from typing import List

class Solution:
    def reorderOddEven(self, nums: List[int]):
        if not nums:
            return
        i = 0
        j = len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 != 0:
                i += 1
            while i< j and nums[j] & 1 == 0:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

nums = [1,2,3,4,5]
Solution().reorderOddEven(nums)
print(nums)
