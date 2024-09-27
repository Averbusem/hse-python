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


""" 
# or slower
class Solution(object):
    def addSpaces(self, s, spaces):
        result = []
        set_spaces = set(spaces)
        for i in range(len(s)):
            if i in set_spaces:
                result.append(" ")
            result.append(s[i])
        return "".join(result)
"""


"""
# Time Limit Exceeded
class Solution(object):
    def addSpaces(self, s, spaces):

        shift = 0
        for i in spaces:
            s = s[: i + shift] + " " + s[i + shift :]
            shift += 1
        return s
"""

sol = Solution()
print(sol.addSpaces("icodeinpython", [1, 5, 7, 9]))
