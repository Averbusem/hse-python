"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        cur_count_vowels = 0
        for i in range(k):
            if s[i] in "aeiou":
                cur_count_vowels += 1
        max_vowels = max(max_vowels, cur_count_vowels)

        left = 0
        for right in range(k, len(s)):
            if s[left] in "aeiou":
                cur_count_vowels -= 1
            if s[right] in "aeiou":
                cur_count_vowels += 1
            max_vowels = max(max_vowels, cur_count_vowels)
            left += 1
        return max_vowels


sol = Solution()
print(sol.maxVowels("leetcode", 3))
