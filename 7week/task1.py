"""
https://leetcode.com/problem-list/sliding-window/
URL: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        res = 0

        cnt = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] == max_elem:
                cnt += 1

            while cnt == k:
                if nums[left] == max_elem:
                    cnt -= 1
                left += 1
            res += left
        return res
