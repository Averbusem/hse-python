"""
https://leetcode.com/problem-list/sliding-window/
URL: https://leetcode.com/problems/count-number-of-nice-subarrays/description/
"""

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        count_odd = 0
        sub_count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                count_odd += 1
                sub_count = 0

            while count_odd == k:
                sub_count += 1
                if nums[left] % 2 != 0:
                    count_odd -= 1
                left += 1

            res += sub_count

        return res


sol = Solution()
print(sol.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
