"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1393342038/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        visited = set()
        maxcnt = 0
        for right in range(len(s)):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            maxcnt = max(maxcnt, right - left + 1)
        return maxcnt
