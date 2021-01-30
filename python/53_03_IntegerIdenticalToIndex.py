# 题目： 数组中数值和下标相等的元素
# 假设一个单调递增的数组中的每个元素都是整数并且是惟一的。请编写一个函数，
# 找出数组中任意一个数值等于其下标的元素。例如，在数组[-3,-1,1,3,5]中，数字
# 3和它的下标相等。
from typing import List


class Solution:
    def findNumEqIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                start = mid + 1
            else:
                end = mid - 1
        return -1


nums = [-3, -1, 1, 3, 5]
print(Solution().findNumEqIndex(nums))
