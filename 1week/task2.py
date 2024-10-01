"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def longestPalindrome(self, s):
        def expandPalindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        start, end = 0, 0  # начало и конец самого длинного палиндрома
        for i in range(len(s)):
            left, right = i, i
            len1 = expandPalindrome(left, right)
            len2 = expandPalindrome(left, right + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]
