"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_len = float("inf")
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= target and left < len(nums) and left < right:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float("inf") else 0


sol = Solution()
print(sol.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
