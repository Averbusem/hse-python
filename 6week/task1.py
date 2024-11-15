"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

import string


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_set = set()
        left = 0
        max_len = 0
        for right in range(len(s)):
            while s[right] in letters_set:
                letters_set.remove(s[left])
                left += 1
            letters_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
