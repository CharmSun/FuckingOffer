# 题目：数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

from typing import List

# 解法一：利用快排的思想，找到 mid 位置的数（leetcode 会超时）


class Solution:

    def partition1(self, nums, start, end) -> int:
        pivot = nums[start]
        l, r = start, end
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            while l < r and nums[l] <= pivot:
                l += 1
            if l < r:
                nums[l], nums[r] = nums[r], nums[l]
        nums[start], nums[r] = nums[r], nums[start]
        return r

    def partition2(self, nums, start, end) -> int:
        pivot = nums[end]
        pos = start - 1
        for i in range(start, end):
            if nums[i] < pivot:
                pos += 1
                if pos != i:
                    nums[pos], nums[i] = nums[i], nums[pos]
        pos += 1
        nums[pos], nums[start] = nums[start], nums[pos]
        return pos

    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        start = 0
        end = len(nums) - 1
        mid = len(nums) >> 1
        index = self.partition1(nums, start, end)
        while index != mid:
            if index > mid:
                end = index - 1
                index = self.partition1(nums, start, end)
            else:
                start = index + 1
                index = self.partition1(nums, start, end)
        return nums[mid]


# 解法2，摩尔投票法
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            elif nums[i] == res:
                count += 1
            else:
                count -= 1
        return res
