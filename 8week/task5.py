"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/submissions/1467785710/
"""

from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            is_consecutive = True
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    is_consecutive = False
                    break

            if is_consecutive:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)

        return result


sol = Solution()
print(sol.resultsArray([1, 2, 3, 4, 3, 2, 5], 3))
