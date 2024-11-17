"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List

# from collections import Counter

""" slow approach
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        nums_counter = Counter()
        cur_sum = 0
        max_sum = 0

        # first subarray
        for i in range(k):
            cur_sum += nums[i]
            nums_counter[nums[i]] += 1
        if len(nums_counter) == k:
            max_sum = max(max_sum, cur_sum)

        # others subarray
        left = 0
        for right in range(k, len(nums)):
            cur_sum -= nums[left]
            cur_sum += nums[right]
            nums_counter[nums[left]] -= 1
            if nums_counter[nums[left]] == 0:
                del nums_counter[nums[left]]
            nums_counter[nums[right]] += 1
            if len(nums_counter) == k:
                max_sum = max(max_sum, cur_sum)
            left += 1
        return max_sum
"""


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return 0

        current_sum = 0
        max_sum = 0
        window_set = set()
        left = 0

        for right in range(len(nums)):
            while nums[right] in window_set:
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            window_set.add(nums[right])
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)
                window_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

        return max_sum


sol = Solution()
print(sol.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3))
