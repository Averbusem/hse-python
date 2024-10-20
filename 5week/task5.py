"""
https://leetcode.com/problem-list/hash-table/?difficulty=MEDIUM
URL: https://leetcode.com/problems/custom-sort-string/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        priority = {letter: i for i, letter in enumerate(order)}
        sorted_str = sorted(s, key=lambda x: priority.get(x, len(order)))
        return "".join(sorted_str)


sol = Solution()
print(sol.customSortString("cba", "abcd"))
