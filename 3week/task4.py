"""
https://leetcode.com/problem-list/array/?difficulty=MEDIUM
URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=problem-list-v2&envId=array&difficulty=MEDIUM
"""

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate_postfix(a, b, operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            else:
                return int(a / b)

        stack = []
        for num in tokens:
            if num in "+-*/":
                b = int(stack.pop())
                a = int(stack.pop())
                res = calculate_postfix(a, b, num)
                stack.append(res)
            else:
                stack.append(int(num))
        return stack[0]


sol = Solution()
print(sol.evalRPN(["18"]))
