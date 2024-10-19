"""
https://leetcode.com/problem-list/hash-table/
URL: https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        table = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000],
        ]

        for letter, val in reversed(table):
            if num // val:
                cnt = num // val
                res += letter * cnt
                num = num % val
        return res
