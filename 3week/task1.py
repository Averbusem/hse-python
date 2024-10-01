"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/merge-intervals/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for pair in intervals:
            if not result or pair[0] > result[-1][1]:
                result.append(pair)
            else:
                result[-1][1] = max(result[-1][1], pair[1])
        return result


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1, 5], [2, 6], [3, 4], [8, 10], [15, 18]]
