# 题目：第一个只出现一次的字符
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in s:
            if dic[ch] == 1:
                return ch
        return ' '
