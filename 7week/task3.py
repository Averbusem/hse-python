"""
https://leetcode.com/problem-list/sliding-window/
URL: https://leetcode.com/problems/repeated-dna-sequences/
"""

from collections import defaultdict
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        sequence_count = defaultdict(int)
        repeated_sequences = []

        for i in range(len(s) - 9):
            substring = s[i : i + 10]
            sequence_count[substring] += 1

            if sequence_count[substring] == 2:
                repeated_sequences.append(substring)

        return repeated_sequences
