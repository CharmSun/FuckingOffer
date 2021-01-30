# 题目：数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。
from typing import List


class Solution:
    # 思想: 归并排序
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        copy = [0] * n
        return self.countPairsWithMergeSort(nums, copy, 0, n-1)

    def countPairsWithMergeSort(self, nums, copy, start, end) -> int:
        if start == end:
            return 0
        mid = (start + end) // 2
        left = self.countPairsWithMergeSort(nums, copy, start, mid)
        right = self.countPairsWithMergeSort(nums, copy, mid+1, end)

        i, j, k = mid, end, end
        count = 0
        while i >= start and j >= mid + 1:
            if nums[i] > nums[j]:
                copy[k] = nums[i]
                count += j - mid
                i -= 1
            else:
                copy[k] = nums[j]
                j -= 1
            k -= 1
        while i >= start:
            copy[k] = nums[i]
            k -= 1
            i -= 1
        while j >= mid + 1:
            copy[k] = nums[j]
            k -= 1
            j -= 1
        for k in range(start, end+1):
            nums[k] = copy[k]
        return left + right + count

nums = [7,5,6,4]
print(Solution().reversePairs(nums))