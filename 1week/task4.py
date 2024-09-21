"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/?envType=problem-list-v2&envId=string
"""


class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1
        result = ""
        for elem in s:
            if len(result) == 0 and elem == " ":
                continue
            elif elem in "+-" and len(result) == 0:
                result += elem
            elif elem.isdigit():
                result += elem
            else:
                break
        if result in "+-":
            return 0
        result_int = int(result)
        if result_int < INT_MIN:
            result_int = INT_MIN
        elif result_int > INT_MAX:
            result_int = INT_MAX
        return result_int


stroka = " -45-6iiou"
sol = Solution()
print(sol.myAtoi(stroka))
