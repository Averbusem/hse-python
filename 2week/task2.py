"""
https://leetcode.com/problem-list/string/
URL: https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        reversed_words = words[::-1]
        output = " ".join(reversed_words)
        return output


""" 2 variant
class Solution(object):
    def reverseWords(self, s):

        words = s.split()
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        output = " ".join(words)
        return output
"""

sol = Solution()
print(sol.reverseWords("  hello   world  "))
