# 题目：最长不含重复字符的子字符串
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

# 动态规划，f(i)表示第i个字符结尾的不含包重复字符的子字符串的最长长度
# 第i个字符没有出现过，f(i)=f(i-1)+1
# 出现过，且距上一个相同字符的距离d > f(i-1), 则f(i) = f(i-1) + 1, 否则f(i) = d

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curLen = 0
        maxLen = 0
        dic = {}
        for i in range(len(s)):
            prevIndex = dic.get(s[i], -1)
            if prevIndex < 0 or i - prevIndex > curLen:
                curLen += 1
            else:
                curLen = i - prevIndex
            dic[s[i]] = i
            if curLen > maxLen:
                maxLen = curLen
        return maxLen
