"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {"a": 0, "b": 0, "c": 0}
        left = 0
        res = 0
        n = len(s)
        for right in range(n):
            count[s[right]] += 1

            while count["a"] > 0 and count["b"] > 0 and count["c"] > 0:
                res += n - right
                count[s[left]] -= 1
                left += 1

        return res


sol = Solution()
print(sol.numberOfSubstrings("abcabc"))
