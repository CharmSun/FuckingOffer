# 题目：0~n-1中缺失的数字
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] != mid:
                if (mid > 0 and nums[mid-1] == mid - 1) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
        if start == len(nums):
            return len(nums)
        return -1