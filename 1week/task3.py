"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                max_len = max(max_len, i - stack[-1])
        return max_len
