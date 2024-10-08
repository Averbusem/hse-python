"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/4sum-ii/description/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        result = 0
        n = len(nums1)
        sum_dict = dict()
        # nums1 and nums2
        for i in range(n):
            for j in range(n):
                cur_sum = nums1[i] + nums2[j]
                if cur_sum not in sum_dict:
                    sum_dict[cur_sum] = 0
                sum_dict[cur_sum] += 1

        # nums3 and nums4
        for i in range(n):
            for j in range(n):
                cur_sum = nums3[i] + nums4[j]
                if -cur_sum in sum_dict:
                    result += sum_dict[-cur_sum]
        return result


sol = Solution()

print(sol.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
