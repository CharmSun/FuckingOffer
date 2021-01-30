# 翻转字符串
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]) # 剔除所有空格字符返回数组并反转，以空格为间隔把数组拼成字符串
