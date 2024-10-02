"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/sort-colors/solutions/5580767/video-2-solutions-with-frequency-or-3-pointers/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1
        index = 0
        for i in range(len(count)):
            for _ in range(count[i]):
                nums[index] = i
                index += 1
