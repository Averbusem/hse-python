"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/search-in-rotated-sorted-array/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid_index = (left + right) // 2

            if nums[mid_index] == target:
                return mid_index

            if nums[left] <= nums[mid_index]:
                if nums[left] <= target < nums[mid_index]:
                    right = mid_index - 1
                else:
                    left = mid_index + 1
            else:
                if nums[mid_index] < target <= nums[right]:
                    left = mid_index + 1
                else:
                    right = mid_index - 1
        return -1


sol = Solution()
print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))
