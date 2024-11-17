"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_len = 0
        set_vowels = set()
        left = 0
        for right in range(len(word)):
            if right > 0 and word[right] >= word[right - 1]:
                set_vowels.add(word[right])
                if len(set_vowels) == 5:
                    max_len = max(max_len, right - left + 1)
            if word[right] < word[right - 1]:
                left = right
                set_vowels.clear()
                set_vowels.add(word[right])
        return max_len


sol = Solution()
print(sol.longestBeautifulSubstring("aeiaaioaaaaeiiiiouuuooaauuaeiu"))
