"""
https://leetcode.com/problem-list/sliding-window/
URL: https://leetcode.com/problems/arithmetic-slices/submissions/1461901750/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0

        max_slices = 0
        cur_slices = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur_slices += 1
                max_slices += cur_slices
            else:
                cur_slices = 0

        return max_slices
