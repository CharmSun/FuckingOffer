#  题目一：找出数组中重复的数字
# 在一个长度为n的数组里的所有数字都在 0~n-1 范围内。数组中
# 某些数字是重复的，不知道有几个数字重复，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，
# 那么对应的输出是重复的数字2或者3

#  题目二：不修改数组找出重复的数字
# 在一个长度为 n+1 的数组里的所有数字都在 1~n 的范围内，所以数组
# 中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能
# 修改输入的数组。例如，如果输入长度为8 的数组「2,3,5,4,3,2,6,7」，那么
# 对应的输出是重复的数字2 或者3

from typing import List


class Solution:

    def duplicate1(self, nums: List[int]) -> int:
        if not nums:
            return -1
        for num in nums:
            if num < 0 or num > len(nums) - 1:
                return -1
        for i in range(len(nums)):
            while nums[i] != i:
                cur = nums[i]
                if cur == nums[cur]:
                    return cur
                nums[i] = nums[cur]
                nums[cur] = cur
        return -1

    # 二分查找
    def duplicate2(self, nums: List[int]) -> int:
        if not nums:
            return -1
        start = 1
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            count = self.countRange(nums, start, mid)
            if start == end:
                if count > 1:
                    return start
                else:
                    break
            if count > mid - start + 1:
                end = mid
            else:
                start = mid + 1
        return -1

    def countRange(self, nums: List[int], start, end) -> int:
        if not nums:
            return 0
        count = 0
        for num in nums:
            if num >= start and num <= end:
                count += 1
        return count


nums1 = [2, 3, 1, 0, 2, 5, 3]
print(Solution().duplicate1(nums1))

nums2 = [2, 3, 5, 4, 3, 2, 6, 7]
print(Solution().duplicate2(nums2))
