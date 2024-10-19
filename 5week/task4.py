"""
https://leetcode.com/problem-list/hash-table/?difficulty=MEDIUM
URL: https://leetcode.com/problems/find-duplicate-file-in-system/description/?envType=problem-list-v2&envId=hash-table&difficulty=MEDIUM
"""

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents_dict = defaultdict(list)
        for elements in paths:
            elements = elements.split()
            path = elements[0]
            for i in range(1, len(elements)):
                name, content = elements[i].split("(")
                contents_dict[content].append(path + "/" + name)

        return [group for group in contents_dict.values() if len(group) > 1]


sol = Solution()
print(
    sol.findDuplicate(
        [
            "root/a 1.txt(abcd) 2.txt(efgh)",
            "root/c 3.txt(abcd)",
            "root/c/d 4.txt(efgh)",
            "root 4.txt(efgh)",
        ]
    )
)
