# 题目：扑克牌中的顺子
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        numberOfZero = 0
        numberOfGap = 0
        for num in nums:
            if num == 0:
                numberOfZero += 1
        small = numberOfZero
        big = small + 1
        while big < len(nums):
            if nums[small] == nums[big]:
                return False
            numberOfGap += nums[big] - nums[small] - 1
            small += 1
            big += 1
        return numberOfGap <= numberOfZero


print(Solution().isStraight([0, 0, 1, 2, 5]))
