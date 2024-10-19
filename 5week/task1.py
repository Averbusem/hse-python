"""
https://leetcode.com/problem-list/hash-table/
URL: https://leetcode.com/problems/majority-element-ii/
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        frequency_letters = dict()
        n = len(nums)
        n3 = n / 3
        for num in nums:
            if num not in frequency_letters:
                frequency_letters[num] = [0, 0]
            frequency_letters[num][0] += 1
            if frequency_letters[num][0] > n3 and frequency_letters[num][1] == 0:
                frequency_letters[num][1] = 1
                result.append(num)
        return result


sol = Solution()
print(sol.majorityElement([1]))
