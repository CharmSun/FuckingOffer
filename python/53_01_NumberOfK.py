# 题目：在排序数组中查找数字
# 统计一个数字在排序数组中出现的次数。
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        first = self.getFirst(nums, target)
        last = self.getLast(nums, target)
        if first > -1 and last > -1:
            return last - first + 1
        return 0
    
    def getFirst(self, nums, target) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if (mid > 0 and nums[mid-1] != target) or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1
    
    def getLast(self, nums, target) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                if (mid < len(nums) - 1 and nums[mid+1] != target) or mid == len(nums) - 1:
                    return mid
                else:
                    start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

nums = [5,7,7,8,8,10]
target = 6
print(Solution().search(nums, target))