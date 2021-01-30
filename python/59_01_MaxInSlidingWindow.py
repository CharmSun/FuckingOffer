# 题目：滑动窗口的最大值
# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
from typing import List
from collections import deque


class Solution:
    # 双端队列，存放有可能成为滑动窗口最大值数值的下标。
    # 队头为滑动窗口最大值的下标
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums or k < 1 or k > len(nums):
            return res
        window = deque([])
        for i, num in enumerate(nums):
            if window and i - window[0] >= k:
                window.popleft()
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


nums = [2, 3, 4, 2, 6, 2, 5, 1]
print(Solution().maxSlidingWindow(nums, 3))
