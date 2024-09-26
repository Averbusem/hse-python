"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def letterCombinations(self, digits):
        # :type digits: str
        # :rtype: List[str]

        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        output = []

        def backtracking(i, temp_str):
            if len(temp_str) == len(digits):
                output.append(temp_str)
                # print(temp_str)
                return
            for letter in keyboard[digits[i]]:
                backtracking(i + 1, temp_str + letter)

        if digits:
            backtracking(0, "")
        return output


sol = Solution()
sol.letterCombinations("234")
