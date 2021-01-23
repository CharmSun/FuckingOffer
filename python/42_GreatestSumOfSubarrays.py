# 题目： 连续子数组的最大和
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
# 要求时间复杂度为O(n)。
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = cur = nums[0]
        for i in range(1, len(nums)):
            if cur <= 0:
                cur = nums[i]
            else:
                cur += nums[i]
            res = max(res, cur)
        return res

print(Solution().maxSubArray([-1]))