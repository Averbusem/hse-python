"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/group-anagrams/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in dictionary:
                dictionary[sorted_str].append(s)
            else:
                dictionary[sorted_str] = [s]
        return list(dictionary.values())


sol = Solution()
res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
