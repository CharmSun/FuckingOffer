# 题目：最小的k个数
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，
# 则最小的4个数字是1、2、3、4。
from typing import List

# 同样利用快排的partition方法
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not arr or k > len(arr) or k < 1:
            return []
        start = 0
        end = len(arr) - 1
        index = self.partition1(arr, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition1(arr, start, end)
            else:
                start = index + 1
                index = self.partition1(arr, start, end)
        return arr[0:k]

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
