"""
https://leetcode.com/problem-list/string/?difficulty=MEDIUM
URL: https://leetcode.com/problems/adding-spaces-to-a-string/
"""


class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        prev = 0

        for i in spaces:
            result.append(s[prev:i])
            result.append(" ")
            prev = i
        result.append(s[prev:])
        return "".join(result)


sol = Solution()
print(sol.addSpaces("icodeinpython", [1, 5, 7, 9]))
