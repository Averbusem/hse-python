"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
"""

from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        set_nums = set(nums)
        cur_counter = Counter()
        left = 0
        for right in range(n):
            cur_counter[nums[right]] += 1
            while len(cur_counter) == len(set_nums):
                res += n - right
                cur_counter[nums[left]] -= 1
                if cur_counter[nums[left]] == 0:
                    del cur_counter[nums[left]]
                left += 1
        return res
