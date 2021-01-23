# 题目：旋转数组的最小数字
# 注意，数字元素可能会有重复的情况

from typing import List

class Solution:

    # 二分查找, 最小值在右半部分第一个
    # 小于right, 缩小right = mid
    # 大于right, 增大left = mid + 1
    # 相等时，缩小right -= 1
    # 循环终止，取left
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]

input = [1,1,1,0,1]
print(Solution().findMin(input))