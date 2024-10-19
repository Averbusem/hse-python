"""
https://leetcode.com/problem-list/hash-table/?difficulty=MEDIUM
URL: https://leetcode.com/problems/html-entity-parser/
"""


class Solution:
    def entityParser(self, text: str) -> str:
        res = (
            text.replace("&quot;", '"')
            .replace("&apos;", "'")
            .replace("&gt;", ">")
            .replace("&lt;", "<")
            .replace("&frasl;", "/")
            .replace("&amp;", "&")
        )
        return res
