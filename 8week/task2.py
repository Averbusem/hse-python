"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        current_sum = sum(arr[:k])
        count = 0

        if current_sum / k >= threshold:
            count += 1

        for i in range(k, len(arr)):
            current_sum += arr[i] - arr[i - k]
            if current_sum / k >= threshold:
                count += 1

        return count


sol = Solution()
print(sol.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
