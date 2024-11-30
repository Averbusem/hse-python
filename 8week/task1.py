"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_count = Counter()

        for i in range(len(s) - minSize + 1):
            substring = s[i : i + minSize]

            if len(set(substring)) <= maxLetters:
                substring_count[substring] += 1

        return max(substring_count.values(), default=0)


sol = Solution()
print(sol.maxFreq("aababcaab", 2, 3, 4))
