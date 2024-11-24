"""
https://leetcode.com/problem-list/sliding-window/
URL: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

import collections


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_set = set("aeiou")
        word_set = set(word)

        if not vowel_set.issubset(word_set):
            return 0

        result = 0
        left = 0
        vowel_count = collections.defaultdict(int)
        consonant_count = 0

        for right in range(len(word)):
            char = word[right]
            if char in vowel_set:
                vowel_count[char] += 1
            else:
                consonant_count += 1

            while consonant_count > k:
                left_char = word[left]
                if left_char in vowel_set:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    consonant_count -= 1
                left += 1

            if len(vowel_count) == 5 and consonant_count == k:
                result += 1

                temp_left = left
                temp_consonant_count = consonant_count
                temp_vowel_count = vowel_count.copy()

                while len(temp_vowel_count) == 5 and temp_consonant_count == k:
                    temp_char = word[temp_left]
                    if temp_char in vowel_set:
                        temp_vowel_count[temp_char] -= 1
                        if temp_vowel_count[temp_char] == 0:
                            del temp_vowel_count[temp_char]
                    else:
                        temp_consonant_count -= 1

                    temp_left += 1

                    if len(temp_vowel_count) == 5 and temp_consonant_count == k:
                        result += 1
                    else:
                        break

        return result


sol = Solution()
print(sol.countOfSubstrings("iqeaouqi", 2))
# должно врнуть 3, а возращает 2
