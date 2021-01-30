# 题目：和为 s 的连个数字
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，
# 使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) < 2:
            return None
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                return [nums[l], nums[r]]
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
        return []
