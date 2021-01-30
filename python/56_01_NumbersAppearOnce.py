# 题目：数组中只出现一次的两个数字
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
from typing import List


class Solution:
    # 解法：找到异或结果最右侧的1，根据该位的1，区分数组位两份，两份各含有一个只出现一次的数字
    def singleNumbers(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        resXOR = 0
        for num in nums:
            resXOR ^= num
        right1Num = 1
        while right1Num & resXOR == 0:
            right1Num = right1Num << 1
        num1 = num2 = 0
        for num in nums:
            if num & right1Num:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]


nums = [1, 2, 5, 2]
print(Solution().singleNumbers(nums))
