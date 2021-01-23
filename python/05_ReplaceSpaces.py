# 题目：替换空格
# 请实现一个函数，把字符串中的每个空格替换成“%20”。例如，
# 输入“We are happy”, 则输出“We%20are%20happy”

# 延伸题：有两个排序数组A1和A2,内存在A1的末尾有足够多的空余空间容纳A2.
# 请实现一个函数，把A2中所有数字插入A1中，并且所有的数字是排序的
from typing import List


class Solution:
    # python中可以直接使用内置的 replace 方法
    # C, C++ 中主要考察指针的移动，将字符串从后向前移动
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n - 1
        while k >= 0:
            if j < 0:
                break
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


print(Solution().replaceSpace('We are happy'))
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)
