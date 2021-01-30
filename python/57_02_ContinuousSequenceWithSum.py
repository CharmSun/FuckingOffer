# 题目：和为 s 的连续正数序列
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target < 3:
            return None
        res = []
        small, big = 1, 2
        curSum = small + big
        mid = target // 2
        while small <= mid:
            while curSum > target and small <= mid:
                curSum -= small
                small += 1
            if curSum == target:
                res.append([i for i in range(small, big + 1)])
            big += 1
            curSum += big
        return res

print(Solution().findContinuousSequence(4))
