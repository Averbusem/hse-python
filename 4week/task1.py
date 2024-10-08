"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/search-a-2d-matrix/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                len = 1
                while num + 1 in nums_set:
                    len += 1
                    num += 1
                max_len = max(max_len, len)

        return max_len


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
sol = Solution()
print(sol.longestConsecutive(nums))
